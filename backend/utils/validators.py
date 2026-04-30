"""Input validation utilities."""
from config import Config
from utils.exceptions import InvalidInputError, TextTooLongError, UnsupportedLanguageError


def validate_text(text) -> str:
    if text is None:
        raise InvalidInputError("Text field is required")
    if not isinstance(text, str):
        raise InvalidInputError("Text must be a string")
    if not text.strip():
        raise InvalidInputError("Text cannot be empty")
    if len(text) > Config.MAX_TEXT_LENGTH:
        raise TextTooLongError(
            f"Text exceeds maximum length of {Config.MAX_TEXT_LENGTH} characters"
        )
    return text


def validate_language(language: str) -> str:
    if language not in Config.SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageError(
            f"Language '{language}' not supported. "
            f"Supported: {Config.SUPPORTED_LANGUAGES}"
        )
    return language


def validate_steps(steps) -> list:
    if not isinstance(steps, list):
        raise InvalidInputError("Steps must be a list of function names")
    return [str(s) for s in steps]