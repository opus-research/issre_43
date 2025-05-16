import requests
from urllib.parse import urlparse
from ..config.paths import GITHUB_HEADERS

def is_url_valid(url):
    """Check if a GitHub URL is valid by making a HEAD request."""
    try:
        r = requests.head(url, headers=GITHUB_HEADERS, timeout=5, allow_redirects=True)
        return r.status_code != 404
    except Exception:
        return False

def parse_github_url(url):
    """Parse a GitHub URL into its components."""
    parsed = urlparse(url)
    parts = parsed.path.split("/")
    if len(parts) >= 5:
        return {
            'org': parts[1],
            'repo': parts[2],
            'type': parts[3],
            'commit': parts[4],
            'filename': parts[5] if len(parts) > 5 else None
        }
    return None

def fix_github_url(url, org, repo):
    """Attempt to fix a broken GitHub URL by updating org/repo."""
    parsed = urlparse(url)
    parts = parsed.path.split("/")
    if len(parts) >= 5:
        parts[1] = org
        parts[2] = repo
        fixed_path = "/".join(parts)
        return f"https://github.com{fixed_path}"
    return None 