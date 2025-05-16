from pathlib import Path

def get_project_root():
    """
    Get the absolute path to the project root directory (issre_43).
    This function will work regardless of where the script is run from.
    """
    # Try to find the project root by looking for the issre_43 directory
    current = Path.cwd()
    while current != current.parent:
        if current.name == "issre_43":
            return current
        current = current.parent
    raise RuntimeError("Could not find issre_43 project root directory")

def get_project_paths():
    """
    Get all the main project paths relative to the project root.
    Returns a dictionary with the following paths:
    - root: Project root directory
    - data: Data directory
    - results: Results directory
    - prompts: Prompts directory
    """
    root = get_project_root()
    return {
        "root": root,
        "data": root / "data",
        "results": root / "results",
        "prompts": root / "prompts"
    } 