"""Reusable decorators."""
import time
from functools import wraps
from utils.logger import prep_logger


def timing(func):
    """Log execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        prep_logger.debug(f"{func.__name__} took {elapsed:.2f} ms")
        return result
    return wrapper


def log_calls(func):
    """Log function entry/exit."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        prep_logger.debug(f"→ {func.__name__}")
        try:
            result = func(*args, **kwargs)
            prep_logger.debug(f"← {func.__name__} OK")
            return result
        except Exception as e:
            prep_logger.error(f"✗ {func.__name__}: {e}")
            raise
    return wrapper