from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import mlflow

from src.config import MODELS_DIR, PROCESSED_DATA_DIR
from src.config import MLFLOW_URI, MLFLOW_EXPERIMENT_NAME
from src.utils import load_run_id

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "test_features.csv",
    model_path: Path = MODELS_DIR / "model.pkl",
    predictions_path: Path = PROCESSED_DATA_DIR / "test_predictions.csv",
    mlflow_uri: str = MLFLOW_URI,
    mlflow_experiment_name: str = MLFLOW_EXPERIMENT_NAME,
):
    id = load_run_id()  # Load the run ID saved during training

    mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment(mlflow_experiment_name)
    with mlflow.start_run(run_id=id) as run:
        pass

if __name__ == "__main__":
    app()
