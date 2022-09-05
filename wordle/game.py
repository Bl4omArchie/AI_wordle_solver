from wordle.mword import Wordlist
from random import randint
import requests


"""
Main_gameboard:
    - Automatic game:
        - single solve
        - multiple solve

    - Manual game:
        - play

Attributs available on every class:
- wordlist: a list with all the word from the indicated wordlist
- len_wordlist: the number of word in the wordlist
- word_to_guess: the word to find
- result: the state of every position ('c': letter find, 'm': letter in the wrong place, 'w': incorrect letter)
"""


def get_wordlist(link):
    try:
        return requests.get(link).text.split("\n")   
    except:
        raise ValueError("Your link seem to be incorrect")


class Wordle_main_gameboard():
    def __init__(self, wordlist_link) -> None:
        """ setup the wordlist """

        self.wordlist_obj = Wordlist(get_wordlist(wordlist_link))
        self.word_to_guess = self.wordlist_obj.wordlist[randint(0, self.wordlist_obj.len_wordlist)]
        self.result = ['w'] * 5


    def is_winning(self):
        #check if the game is finished
        return self.result == ['c'] * 5


    def compare(self):
        for i in range(5):
            if self.guess[i] == self.word_to_guess[i]:
                self.result[i] = 'c'

            elif self.guess[i] in self.word_to_guess:
                self.result[i] = 'm'

            else:
                self.result[i] = 'w'


class Manual_game(Wordle_main_gameboard):
    def __init__(self, wordlist_link) -> None:
        super().__init__(wordlist_link)

    def play(self):
        c = 1

        while c < 7:
            end_turn = 0
            while end_turn == 0:
                self.guess = input(f"Turn: {c} Input your 5 letters word guess: ")

                if self.guess not in self.main_wordlist or len(self.guess) != 5:
                    print ("\nNot in word list\n")
                    continue

                end_turn = 1
                self.compare()
                print (f"Result: {self.result}\n")

                c += 1
                if self.is_winning() == True:
                    print ("Congrats, you win !")
                    return 1

        print (f"You lost ! The word was {self.word_to_guess}")