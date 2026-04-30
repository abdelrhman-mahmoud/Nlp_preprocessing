"""Centralized logging setup."""
import logging
from logging.handlers import RotatingFileHandler
from config import Config


def setup_logger(name: str, log_file: str, level: str = "INFO") -> logging.Logger:
    """Create a logger with file + console handlers."""
    formatter = logging.Formatter(
        '%(asctime)s | %(name)-15s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        Config.LOG_DIR / log_file,
        maxBytes=Config.LOG_MAX_SIZE,
        backupCount=Config.LOG_BACKUP,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Pre-configured loggers
app_logger   = setup_logger("app",           "app.log",           Config.LOG_LEVEL)
api_logger   = setup_logger("api",           "api.log",           Config.LOG_LEVEL)
prep_logger  = setup_logger("preprocessing", "preprocessing.log", Config.LOG_LEVEL)
error_logger = setup_logger("error",         "error.log",         "ERROR")