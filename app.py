from wordle.solver import IA_wordle_solver
from wordle.game import Game
import argparse


def play_game(link):                    #gamemod 1
    obj = Game(link)
    obj.play()

def play_bot_game(link):                #gamemod 2
    obj = IA_wordle_solver(link)
    obj.play()

def play_several_bot_game(nb, link):    #gamemod 3
    obj = IA_wordle_solver(link)
    obj.automatic_play(nb)


if __name__ == "__main__":
    """
    fr_link = "https://raw.githubusercontent.com/LouanBen/wordle-fr/main/mots.txt"
    en_link = "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/dde79fe924c5869e18d02d04c26f37db1c3c1553/wordle-nyt-answers-alphabetical.txt"
    
    #Bonus I will maybe add one day
    en_allowed_guess_link = "https://gist.githubusercontent.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f/raw/2f51b4f2bb96c02e1dee37808b2eed4ef23a3150/wordle-nyt-allowed-guesses.txt"
    """

    wordlist_link = "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/dde79fe924c5869e18d02d04c26f37db1c3c1553/wordle-nyt-answers-alphabetical.txt"

    parser = argparse.ArgumentParser(description="Wordle game app", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-g", type=int, help="Chose your gamemod: 1 for normal play, 2 for bot play and 3 for several bot play")
    parser.add_argument("-n", type=int, help="Only for gamemod 3: the number of game for the bot")
    parser.add_argument("-w", help="By default we already have a wordlist, but you still can pick your own one. Indicate your web link")
    args = parser.parse_args()

    if args.g == 1:
        if args.w:
            wordlist_link = args.w
        play_game(wordlist_link)

    elif args.g == 2:
        if args.w:
            wordlist_link = args.w
        play_bot_game(wordlist_link)

    elif args.g == 3:
        try:
            if args.w:
                wordlist_link = args.w
            play_several_bot_game(args.n, wordlist_link)
        except:
            raise ValueError("For gamemod 3, you need to precise the number of game")