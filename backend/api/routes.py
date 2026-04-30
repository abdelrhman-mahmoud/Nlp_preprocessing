"""Flask API routes."""
from flask import Blueprint, request, jsonify
from api.language_detector import LanguageDetector
from api.dialect_detector import ArabicDialectDetector
from pipelines import EnglishPipeline, ArabicPipeline
from utils.logger import api_logger, error_logger
from utils.validators import validate_text, validate_language, validate_steps
from utils.exceptions import NLPException
from config import Config

api_bp = Blueprint("api", __name__)

# Lazy initialization
_pipelines = {}
_dialect_detector = None


def get_pipeline(language: str):
    if language not in _pipelines:
        api_logger.info(f"Initializing pipeline: {language}")
        _pipelines[language] = (
            EnglishPipeline() if language == "en" else ArabicPipeline()
        )
    return _pipelines[language]


def get_dialect_detector():
    global _dialect_detector
    if _dialect_detector is None:
        _dialect_detector = ArabicDialectDetector.get_instance()
    return _dialect_detector


# ==================== ROUTES ====================

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status":              "ok",
        "supported_languages": Config.SUPPORTED_LANGUAGES,
        "supported_dialects":  Config.SUPPORTED_DIALECTS,
    })


@api_bp.route("/detect-language", methods=["POST"])
def detect_language():
    """Detect language (en/ar)."""
    try:
        data = request.get_json() or {}
        text = validate_text(data.get("text"))
        lang = LanguageDetector.detect(text)
        api_logger.info(f"Language detected: {lang}")
        return jsonify({"language": lang})
    except NLPException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        error_logger.exception("detect_language failed")
        return jsonify({"error": str(e)}), 500


@api_bp.route("/detect-dialect", methods=["POST"])
def detect_dialect():
    """Identify Arabic dialect (MSA/EGY/GLF/LEV/NOR)."""
    try:
        data = request.get_json() or {}
        text = validate_text(data.get("text"))
        result = get_dialect_detector().predict(text)
        api_logger.info(f"Dialect: {result['top_dialect']}")
        return jsonify(result)
    except NLPException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        error_logger.exception("detect_dialect failed")
        return jsonify({"error": str(e)}), 500


@api_bp.route("/functions/<language>", methods=["GET"])
def list_functions(language: str):
    """Return all available preprocessing functions for a language."""
    try:
        validate_language(language)
        pipe = get_pipeline(language)
        return jsonify({
            "language":  language,
            "functions": pipe.list_functions(),
            "count":     len(pipe.list_functions()),
        })
    except NLPException as e:
        return jsonify(e.to_dict()), e.status_code


@api_bp.route("/preprocess", methods=["POST"])
def preprocess():
    """
    Main preprocessing endpoint.

    Request JSON:
    {
      "text":       "...",
      "language":   "en" | "ar"  (optional, auto-detect if missing)
      "steps":      ["remove_urls", "lowercase", ...],
      "auto_order": true  (optional, default true)
    }
    """
    try:
        data = request.get_json() or {}
        text       = validate_text(data.get("text"))
        steps      = validate_steps(data.get("steps", []))
        auto_order = bool(data.get("auto_order", True))

        # Auto-detect language if not provided
        language = data.get("language") or LanguageDetector.detect(text)
        validate_language(language)

        # Run pipeline
        pipe   = get_pipeline(language)
        result = pipe.run(text, steps, auto_order=auto_order)
        result["language"] = language

        # If Arabic, also include dialect info
        if language == "ar":
            try:
                dialect_info = get_dialect_detector().predict(text)
                result["dialect"] = dialect_info
            except Exception:
                pass

        api_logger.info(
            f"Preprocessed: lang={language}, "
            f"applied={len(result['applied'])}, "
            f"skipped={len(result['skipped'])}"
        )
        return jsonify(result)

    except NLPException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        error_logger.exception("preprocess failed")
        return jsonify({"error": str(e)}), 500


@api_bp.route("/preprocess/smart", methods=["POST"])
def preprocess_smart():
    """
    Smart endpoint: auto-detects language + dialect,
    applies recommended default pipeline.
    """
    try:
        data = request.get_json() or {}
        text = validate_text(data.get("text"))

        language = LanguageDetector.detect(text)
        validate_language(language)

        if language == "en":
            steps = [
                "remove_html", "remove_urls", "remove_emoji",
                "expand_contractions", "lowercase",
                "remove_digits", "remove_punctuation",
                "normalize_repetition", "remove_stopwords",
                "lemmatize", "normalize_whitespace",
            ]
            result = get_pipeline("en").run(text, steps)
            result["language"] = "en"

        else:  # Arabic
            dialect_info = get_dialect_detector().predict(text)
            dialect = dialect_info["top_dialect"]
            lemma_step = "lemmatize_egy_camel" if dialect == "EGY" else "lemmatize_msa_camel"

            steps = [
                "remove_urls", "remove_emoji",
                "remove_digits", "remove_punctuation",
                "remove_tashkeel", "remove_tatweel",
                "normalize_repetition", "normalize_camel",
                "remove_stopwords", lemma_step, "normalize_whitespace",
            ]
            result = get_pipeline("ar").run(text, steps)
            result["language"] = "ar"
            result["dialect"]  = dialect_info

        return jsonify(result)

    except NLPException as e:
        return jsonify(e.to_dict()), e.status_code
    except Exception as e:
        error_logger.exception("preprocess_smart failed")
        return jsonify({"error": str(e)}), 500