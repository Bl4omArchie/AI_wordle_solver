from random import randint
import requests


""" A special object for manage the wordlist """

class Wordlist():
    def __init__(self, link) -> None:
        r = requests.get(link)
        self.wlist = r.text.split("\n")
        self.wlist_size = len(self.wlist)

    
    def split_word(self, word): #split every letter of the given word. ex: shark -> ['s', 'h', 'a', 'r', 'k']
        return [*word]

    def word_in_list(self, word):
        return word in self.wlist

    def get_wordle(self):
        return self.wlist[randint(0, self.wlist_size)]