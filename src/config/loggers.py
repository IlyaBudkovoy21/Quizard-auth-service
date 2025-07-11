from pathlib import Path


def configure_logging():
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
