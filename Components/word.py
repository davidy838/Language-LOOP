class Word:
    def __init__(self, english, chinese, pinyin, picture, audio, character):
        self.english = english
        self.chinese = chinese
        self.pinyin = pinyin
        self.picture = picture
        self.audio = audio
        self.character = character

    def repeat(self):
        return f"{self.english} {self.chinese} {self.pinyin} {self.picture} {self.audio} {self.character}"
