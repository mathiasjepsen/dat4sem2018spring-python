import string
import re

class TextContainer():
    def __init__(self, ascii_text):
        self.text = ascii_text

    def get_word_count(self):
        text = "".join(char for char in self.text if char not in string.punctuation ).split(" ")
        return len(text_str) 