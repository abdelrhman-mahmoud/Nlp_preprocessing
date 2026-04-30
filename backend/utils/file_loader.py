"""Load custom resources from /models."""
import json
from pathlib import Path
from utils.logger import app_logger


def load_text_file(path: Path) -> set:
    """Load lines from a text file as a set."""
    if not path.exists():
        app_logger.warning(f"File not found: {path}")
        return set()
    with open(path, encoding='utf-8') as f:
        return {line.strip() for line in f if line.strip()}


def load_json(path: Path) -> dict:
    """Load JSON dictionary."""
    if not path.exists():
        app_logger.warning(f"JSON not found: {path}")
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)