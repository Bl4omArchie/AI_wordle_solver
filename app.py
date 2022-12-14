from src.wordlist import Wordlist
from src.game import Wordle
from src.launcher import *
import argparse

""" The main app where you can acces easily to the different gamemode"""


def start_game(gamemod, link):                    #gamemod 1
    wordlist = Wordlist(link)
    game = Wordle(wordlist)

    if gamemod == 1:
        normal_play(game, wordlist)
    
    elif gamemod == 2:
        AI_play(game, wordlist)


if __name__ == "__main__":
    """
    fr_link = "https://raw.githubusercontent.com/LouanBen/wordle-fr/main/mots.txt"
    en_link = "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/dde79fe924c5869e18d02d04c26f37db1c3c1553/wordle-nyt-answers-alphabetical.txt"
    
    #Bonus words that can be used as a guess for a more accurate answer. Not available now.
    en_allowed_guess_link = "https://gist.githubusercontent.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f/raw/2f51b4f2bb96c02e1dee37808b2eed4ef23a3150/wordle-nyt-allowed-guesses.txt"


    wordlist_link = "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/dde79fe924c5869e18d02d04c26f37db1c3c1553/wordle-nyt-answers-alphabetical.txt"
    """

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

    args = parser.parse_args()

    start_game(wordlist_link)