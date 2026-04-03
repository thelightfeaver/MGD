import os

RUN_FILE = "run_id.txt"

def load_run_id() -> str:
    """
    Load the MLflow run ID from a file. If the file does not exist, return None.

    Returns:
        str: The MLflow run ID, or None if the file does not exist.
    """
    if os.path.exists(RUN_FILE):
        with open(RUN_FILE, "r") as f:
            return f.read().strip()
    return None


def save_run_id(run_id: str):
    """
    Save the MLflow run ID to a file.

    Args:
        run_id (str): The MLflow run ID to be saved.
    """
    with open(RUN_FILE, "w") as f:
        f.write(run_id)