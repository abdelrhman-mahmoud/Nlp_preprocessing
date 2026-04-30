from spellchecker import SpellChecker

class EnglishSpellChecker:
    spell = SpellChecker(language='en')

    @staticmethod
    def correct(text: str) -> str:
        out = []
        for w in text.split():
            c = EnglishSpellChecker.spell.correction(w)
            out.append(c if c else w)
        return ' '.join(out)