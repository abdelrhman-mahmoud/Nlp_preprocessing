import emoji

class EmojiHandler:
    @staticmethod
    def remove(text: str) -> str:
        return emoji.replace_emoji(text, replace='')

    @staticmethod
    def to_text(text: str) -> str:
        return emoji.demojize(text, delimiters=(" ", " "))