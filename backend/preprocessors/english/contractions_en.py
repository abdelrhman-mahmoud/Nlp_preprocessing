import contractions

class ContractionExpander:
    @staticmethod
    def expand(text: str) -> str:
        return contractions.fix(text)