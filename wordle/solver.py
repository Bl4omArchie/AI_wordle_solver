from wordle.game import Wordle_main_gameboard
from wordle.mfreq import Frequency_letter
from wordle.mword import Wordlist
from copy import deepcopy


""" 
IA_autosolver_game:
    - Wordlist: manage the wordlist
    - Frequency_letter: compute all the needed frequency

Specific wordlist for IA_autosolver_game: self.custom_wordlist
"""


class IA_autosolver_game(Wordle_main_gameboard):
    def __init__(self, wordlist_link) -> None:
        super().__init__(wordlist_link)

        self.custom_wordlist = deepcopy(self.wordlist_obj.wordlist)
        self.len_custom_wordlist = self.wordlist_obj.len_wordlist
        self.guess = ""

        self.freq_obj = Frequency_letter(self.wordlist_obj)


    def solver(self):
        """ 
        1) Choisir le mot qui possède le plus de lettre ayant la plus grand probabilité d'apparition à un endroit donné
        2) Emettre le guess
        3) En fonction des résultat update définitivement la wordlist des mots ne pouvant être correct

        """
        self.guess = self.freq_obj.get_most_probable_word()
        self.compare()
        self.update_custom_wordlist()


    def play(self):
        c = 1

        while c < 7:
            self.solver()
            print (f"Turn {c}:\n   Guess: {self.guess}\n   Result: {self.result}\n   Wordlist len: {self.len_custom_wordlist}\n")
            c += 1
            if self.is_winning() == True:
                print (f"You won in {c} rounds")
                return 1

        print (f"All the round are passed, you lost. Word to guess: {self.word_to_guess}")
        return 0


    def automatic_play(self, nb):
        win, lose = 0, 0
        c = 1

        for _ in range(nb):
            while c < 7:
                self.solver()
                c += 1
                if self.is_winning() == True:
                    win += 1
                    break
            lose += 0
        
        print (f"For {nb} games, the bot winned {win} games and lost {lose} games")