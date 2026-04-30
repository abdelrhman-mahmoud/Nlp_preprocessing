"""Application configuration."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    # ==== Paths ====
    BASE_DIR    = Path(__file__).resolve().parent
    LOG_DIR     = BASE_DIR / "logs"
    MODELS_DIR  = BASE_DIR / "models"
    EN_MODELS   = MODELS_DIR / "english"
    AR_MODELS   = MODELS_DIR / "arabic"

    # ==== Server ====
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    HOST  = os.getenv("HOST", "0.0.0.0")
    PORT  = int(os.getenv("PORT", 5000))

    # ==== App ====
    SUPPORTED_LANGUAGES = ["en", "ar"]
    SUPPORTED_DIALECTS  = ["MSA", "EGY", "GLF", "LEV", "NOR"]
    MAX_TEXT_LENGTH     = int(os.getenv("MAX_TEXT_LENGTH", 100_000))

    # ==== Logging ====
    LOG_LEVEL    = os.getenv("LOG_LEVEL", "INFO")
    LOG_MAX_SIZE = 5_000_000
    LOG_BACKUP   = 5

    # ==== CAMeL Tools ====
    CAMEL_MSA_DB = "calima-msa-r13"
    CAMEL_EGY_DB = "calima-egy-r13"

    @classmethod
    def init_dirs(cls):
        """Create required directories."""
        for path in [cls.LOG_DIR, cls.MODELS_DIR, cls.EN_MODELS, cls.AR_MODELS]:
            path.mkdir(parents=True, exist_ok=True)


Config.init_dirs()