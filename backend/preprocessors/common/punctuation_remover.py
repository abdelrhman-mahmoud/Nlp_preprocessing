class PunctuationRemover:
    ARABIC = '،؛؟«»()ـ"\'!.:'
    ALL    = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' + ARABIC

    @staticmethod
    def remove(text: str) -> str:
        return text.translate(str.maketrans('', '', PunctuationRemover.ALL))