from random import randint
import requests


class Wordlist():
    """ A special object for manage the wordlist 
    a Wordlist object is:
        - a wordlist grabbed from a link
        - the size of the wordlist
        - a dictionnary with every words and their stats
        - one random wordle (the word to be guess)
    """

    def __init__(self, link) -> None:
        r = requests.get(link)
        r = r.text.split("\n")
        
        self.word_count = len(r)
        self.to_guess = r[randint(0, self.word_count)]

        self.wdict = {}
        for word in r:
            self.wdict[word] = 1

    
    def split_word(self, word): #split every letter of the given word. ex: shark -> ['s', 'h', 'a', 'r', 'k']
        return [*word]


    def word_in_list(self, word):
        return word in self.wdict
