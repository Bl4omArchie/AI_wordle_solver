from random import randint
import requests


class Wordle():
    def __init__(self, wordlist_link) -> None:
        """ setup the wordlist"""
        r = requests.get(wordlist_link)
        self.word_list = r.text.split("\n")

        self.word_to_guess = self.word_list[randint(0, len(self.word_list))]
        self.result = ['c'] * 5


    def is_winning(self):
        if self.result == ['c'] * 5:
            return 1
        else:
            return 0 

    def compare(self):
        for i in range(5):
            if self.guess[i] == self.word_to_guess[i]:
                self.result[i] = 'c'

            elif self.guess[i] in self.word_to_guess:
                self.result[i] = 'm'

            else:
                self.result[i] = 'w'

    def board(self, guess):
        c = 1
        while c < 7:
            end_turn = 0
            while end_turn == 0:
                self.compare(guess)


class Game(Wordle):
    def __init__(self, wordlist_link) -> None:
        super().__init__(wordlist_link)

    def play(self):
        c = 1

        while c < 7:
            end_turn = 0
            while end_turn == 0:
                self.guess = input(f"Turn: {c} Input your 5 letters word guess: ")

                if self.guess not in self.word_list or len(self.guess) != 5:
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