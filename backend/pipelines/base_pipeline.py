"""Composable pipeline with auto-ordering."""
from utils.logger import prep_logger
from utils.exceptions import PipelineExecutionError


class BasePipeline:
    """
    Pipeline that runs a list of preprocessing functions.
    Supports auto-ordering by recommended sequence.
    """

    DEFAULT_ORDER = [
        # 1. Structural
        "remove_html", "remove_urls", "emoji_to_text", "remove_emoji",
        # 2. Character-level
        "remove_digits", "remove_punctuation",
        "remove_tashkeel", "remove_tatweel",
        "normalize_repetition",
        # 3. Normalization
        "expand_contractions", "lowercase",
        "normalize_basic", "normalize_arabic", "normalize_camel",
        # 4. Correction
        "spell_correct",
        # 5. Stopwords
        "remove_stopwords",
        # 6. Morphological
        "stem", "stem_isri", "stem_light",
        "lemmatize", "lemmatize_qalsadi",
        "lemmatize_msa_camel", "lemmatize_egy_camel",
        # 7. Final
        "normalize_whitespace",
    ]

    def __init__(self, functions: dict):
        self.functions = functions

    def list_functions(self) -> list:
        return list(self.functions.keys())

    def _sort_steps(self, steps: list) -> list:
        order_map = {s: i for i, s in enumerate(self.DEFAULT_ORDER)}
        return sorted(steps, key=lambda s: order_map.get(s, 999))

    def run(self, text: str, steps: list, auto_order: bool = True) -> dict:
        if auto_order:
            steps = self._sort_steps(steps)

        history = [{"step": "input", "text": text}]
        current = text
        applied = []
        skipped = []

        for step in steps:
            if step not in self.functions:
                prep_logger.warning(f"Unknown step skipped: {step}")
                skipped.append(step)
                continue
            try:
                current = self.functions[step](current)
                history.append({"step": step, "text": current})
                applied.append(step)
                prep_logger.info(f"Applied: {step}")
            except Exception as e:
                prep_logger.error(f"Error in {step}: {e}")
                history.append({"step": step, "error": str(e)})
                raise PipelineExecutionError(f"Step '{step}' failed: {e}")

        return {
            "output":  current,
            "history": history,
            "applied": applied,
            "skipped": skipped,
            "order":   steps,
        }