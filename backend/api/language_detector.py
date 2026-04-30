import re
from langdetect import detect, DetectorFactory
from utils.logger import app_logger

DetectorFactory.seed = 0


class LanguageDetector:
    ARABIC_RANGE  = re.compile(r'[\u0600-\u06FF\u0750-\u077F]')
    ENGLISH_RANGE = re.compile(r'[a-zA-Z]')

    @staticmethod
    def detect(text: str) -> str:
        if not text or not text.strip():
            return "unknown"

        ar = len(LanguageDetector.ARABIC_RANGE.findall(text))
        en = len(LanguageDetector.ENGLISH_RANGE.findall(text))

        if ar > en:  return "ar"
        if en > ar:  return "en"

        try:
            lang = detect(text)
            return lang if lang in ["en", "ar"] else "unknown"
        except Exception as e:
            app_logger.warning(f"Language detection failed: {e}")
            return "unknown"