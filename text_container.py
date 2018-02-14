import string

class TextContainer():
    def __init__(self, ascii_text):
        self.text = ascii_text

    def get_word_count(self):
        text = "".join("hej " for word in self.text if word not in string.punctuation).split(" ")
        print(text)
        return len(text)
