from camel_tools.dialectid import DialectIdentifier
from utils.logger import app_logger


class ArabicDialectDetector:
    """Detects Arabic dialect: MSA, EGY, GLF, LEV, NOR."""

    _instance = None

    def __init__(self):
        app_logger.info("Loading dialect identifier...")
        self.did = DialectIdentifier.pretrained()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def predict(self, text: str, top_k: int = 3) -> dict:
        predictions = self.did.predict([text], 'region')
        top = predictions[0]
        return {
            "top_dialect": top.top,
            "scores": dict(sorted(top.scores.items(),
                                  key=lambda x: -x[1])[:top_k]),
        }