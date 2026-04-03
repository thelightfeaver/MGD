from pathlib import Path

import mlflow
import typer
from loguru import logger
from tqdm import tqdm

from src.config import (MLFLOW_EXPERIMENT_NAME, MLFLOW_URI, MODELS_DIR,
                        PROCESSED_DATA_DIR)
from src.utils import save_run_id

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "features.csv",
    labels_path: Path = PROCESSED_DATA_DIR / "labels.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    mlflow_uri: str = MLFLOW_URI,
    mlflow_experiment_name: str = MLFLOW_EXPERIMENT_NAME,
):

    mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment(mlflow_experiment_name)
    mlflow.autolog(silent=True)  # Automatically log parameters, metrics, and artifacts
    with mlflow.start_run() as run:
        save_run_id(run.info.run_id)  # Save the run ID for later use in prediction
        mlflow.log_param("example_param", "example_value")  # Example of logging a parameter


if __name__ == "__main__":
    app()
