import json
import os
import time
import asyncio
from openai import AsyncOpenAI
import openai
import tiktoken
from dotenv import load_dotenv
from pathlib import Path

from utils.rate_limiter import RateLimiter
from utils.paths import get_project_paths

# Get project paths
PATHS = get_project_paths()
DATA_DIR = PATHS["data"]
RESULTS_DIR = PATHS["results"]
PROMPTS_DIR = PATHS["prompts"]

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
projects_file = DATA_DIR / "raw" / "projects_by_language.json"
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Default to gpt-4o if not specified

def extract_json_from_code_block(text):
    if text.startswith("```json") or text.startswith("```"):
        return text.strip("```json").strip("```").strip()
    return text

def load_and_merge_raw_batches(batch_folder):
    merged_results = []

    batch_files = sorted([f for f in os.listdir(batch_folder) if f.endswith(".txt")])
    for batch_file in batch_files:
        with open(os.path.join(batch_folder, batch_file), "r", encoding="utf-8") as f:
            raw_text = f.read()
            cleaned_text = extract_json_from_code_block(raw_text)

            try:
                parsed = json.loads(cleaned_text)
                merged_results.extend(parsed)
            except json.JSONDecodeError:
                print(f"⚠️ JSON inválido em {batch_file}, pulando...")

    return merged_results

# Function to format PR data for prompt
def prepare_textual_prs(pr_data):
    return [
        {
            "pull_request_id": str(pr["_id"]),
            #"body": pr["body"],
            #"head_branch": pr["head_branch"],
            "comments": pr["comments"],
            #"commit_messages": pr["commit_messages"]
        }
        for pr in pr_data
    ]

# Evaluate local boolean guidelines
def evaluate_booleans_locally(pr_data):
    results = {}
    for pr in pr_data:
        results[str(pr["_id"])] = {
            "Write Automated Tests": "yes" if pr["has_test_file"] else "no",
            "Document Your Changes": "yes" if pr["documentation_file_was_changed"] or pr["documentation_or_comments_in_code_were_changed"] else "no",
            "Fork and Clone the Repository": "yes" if pr["is_a_fork"] else "no"
        }
    return results

def count_tokens(text, model=MODEL):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def split_prs_smart(textual_prompt, guidelines, prs, target_tokens=40000):
    batches = []
    current_batch = []
    current_tokens = count_tokens(textual_prompt) + count_tokens(json.dumps(guidelines))

    for pr in prs:
        pr_text = json.dumps(pr)
        pr_tokens = count_tokens(pr_text)

        if current_tokens + pr_tokens > target_tokens:
            batches.append(current_batch)
            current_batch = []
            current_tokens = count_tokens(textual_prompt) + count_tokens(json.dumps(guidelines))

        current_batch.append(pr)
        current_tokens += pr_tokens

    if current_batch:
        batches.append(current_batch)

    return batches

def safe_openai_call(messages, model=MODEL, retries=5, sleep_base=10):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.2
            )
            return response.choices[0].message.content

        except openai.RateLimitError as e:
            wait_time = sleep_base * (attempt + 1)
            print(f"⚠️ Rate limit error. Waiting {wait_time}s before retrying...")
            time.sleep(wait_time)

        except openai.BadRequestError as e:
            if "context_length_exceeded" in str(e):
                raise ValueError("Context length exceeded. Need to shrink batch size!")
            else:
                raise e  # other 400 errors, rethrow

        except openai.Timeout as e:
            wait_time = sleep_base * (attempt + 1)
            print(f"⚠️ Timeout. Waiting {wait_time}s before retrying...")
            time.sleep(wait_time)

    raise RuntimeError("⛔ Exceeded maximum retries for OpenAI call.")


def load_raw(owner, repo):
    # Carrega dados dos PRs para extrair campos booleanos
    with open(DATA_DIR / "pull_requests" / f"{owner}_{repo}_aggregated_issues.json") as f:
        pr_data = json.load(f)

    # Gera os resultados booleanos
    boolean_results = evaluate_booleans_locally(pr_data)

    # Lê os resultados textuais dos batches
    batch_folder = RESULTS_DIR / "rq2" / f"{repo}_raw_batches"
    textual_results = load_and_merge_raw_batches(batch_folder)

    # Junta os dois
    final_output = []
    for result in textual_results:
        pr_id = result["pull_request_id"]
        compliance = result["guideline_compliance"]

        if pr_id in boolean_results:
            compliance.update(boolean_results[pr_id])

        final_output.append({
            "pull_request_id": pr_id,
            "guideline_compliance": compliance,
            "merged": ""
        })

    # Salva o resultado final
    with open(RESULTS_DIR / "rq2" / f"{repo}_guideline_compliance_output.json", "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2)

    print("✅ JSON final unificado com textuais + booleanos salvo!")

def count_tokens(text, model=MODEL):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

# === Extract JSON from markdown block ===
def extract_json_from_code_block(text):
    if text.startswith("```json") or text.startswith("```"):
        return text.strip("```json").strip("```").strip()
    return text

# === Split PRs into batches ===
def split_prs_smart(textual_prompt, guidelines, prs, max_input_tokens=60000):
    batches = []
    current_batch = []
    prompt_tokens = count_tokens(textual_prompt) + count_tokens(json.dumps(guidelines))
    current_tokens = prompt_tokens

    for pr in prs:
        pr_text = json.dumps(pr)
        pr_tokens = count_tokens(pr_text)

        if current_tokens + pr_tokens > max_input_tokens:
            batches.append(current_batch)
            current_batch = []
            current_tokens = prompt_tokens

        current_batch.append(pr)
        current_tokens += pr_tokens

    if current_batch:
        batches.append(current_batch)

    return batches

# === Async evaluator for one batch ===
async def evaluate_batch(i, batch, project_name, textual_prompt, guidelines, rate_limiter, client, semaphore):
    output_dir = RESULTS_DIR / "rq2" / f"{project_name}_raw_batches"
    os.makedirs(output_dir, exist_ok=True)
    batch_path = output_dir / f"batch_{i+1}.txt"

    if os.path.exists(batch_path):
        print(f"✅ {project_name} - Batch {i+1} already exists. Skipping.")
        return []

    messages = [
        {"role": "system", "content": textual_prompt},
        {"role": "user", "content": f"### Guidelines:\n{json.dumps(guidelines)}\n\n### Pull Requests:\n{json.dumps(batch)}"}
    ]
    prompt_text = messages[0]["content"] + messages[1]["content"]
    token_count = count_tokens(prompt_text)

    while not rate_limiter.can_send(token_count):
        await asyncio.sleep(0.5)

    rate_limiter.consume(token_count)

    async with semaphore:
        try:
            response = await client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.2,
                max_tokens=16384
            )
            reply = response.choices[0].message.content
            with open(batch_path, "w", encoding="utf-8") as f:
                f.write(reply)
            reply_json = extract_json_from_code_block(reply)
            return json.loads(reply_json)
        except Exception as e:
            print(f"❌ Error in {project_name} batch {i+1}: {e}")
            return []

# === Master runner ===
async def main():
    # Load projects and guidelines
    with open(projects_file, "r", encoding="utf-8") as f:
        projects = json.load(f)["projects"]

    with open(RESULTS_DIR / "rq1" / "guidelines_textual.json", "r", encoding="utf-8") as f:
        guidelines = json.load(f)['response']['final_guidelines']

    with open(PROMPTS_DIR / "openai_rq2.txt", "r", encoding="utf-8") as f:
        textual_prompt = f.read()

    # Initialize OpenAI client and rate limiter
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    rate_limiter = RateLimiter()
    semaphore = asyncio.Semaphore(100)
    tasks = []

    # Process each project
    for project in projects:
        owner = project["owner"]
        repo = project["repo"]
        project_name = f"{owner}_{repo}"

        path = DATA_DIR / "pull_requests" / f"{owner}_{repo}_aggregated_issues.json"
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            pr_data = json.load(f)

        # Prepare PRs for evaluation
        textual_prs = prepare_textual_prs(pr_data)
        batches = split_prs_smart(textual_prompt, guidelines, textual_prs)

        # Create tasks for each batch
        for i, batch in enumerate(batches):
            task = evaluate_batch(i, batch, project_name, textual_prompt, guidelines, rate_limiter, client, semaphore)
            tasks.append(task)

    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Process results for each project
    for project in projects:
        owner = project["owner"]
        repo = project["repo"]
        load_raw(owner, repo)

if __name__ == "__main__":
    asyncio.run(main())
