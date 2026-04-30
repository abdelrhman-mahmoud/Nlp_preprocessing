"""Custom exceptions."""


class NLPException(Exception):
    """Base exception for the application."""
    status_code = 500

    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return {"error": self.message, "type": self.__class__.__name__}


class UnsupportedLanguageError(NLPException):
    status_code = 400


class InvalidInputError(NLPException):
    status_code = 400


class PipelineExecutionError(NLPException):
    status_code = 500


class TextTooLongError(NLPException):
    status_code = 413