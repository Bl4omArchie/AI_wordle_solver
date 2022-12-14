from random import randint
import requests


""" A special object for manage the wordlist """

class Wordlist():
    def __init__(self, link) -> None:
        r = requests.get(link)
        self.word_list = r.text.split("\n")
        
        for i in range(len(self.word_list)):
            self.word_list[i] = [*self.word_list[i]]



    def get_wordle(self):
        return self.word_list[randint(0, len(self.word_list))]