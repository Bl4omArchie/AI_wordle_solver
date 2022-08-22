from wordle.game import Wordle
from copy import deepcopy


class IA_wordle_solver(Wordle):
    def __init__(self, wordlist_link) -> None:
        super().__init__(wordlist_link)
        self.compute_wordlist_frequency()
        self.custom_wordlist = deepcopy(self.word_list)

    def compute_wordlist_frequency(self):
        """
        We computing the occurency of each letter in the wordlist
        Then, we the following formula: occurency * 100 / total of all occurency 
        We get the frenquency value of each letter
        """
        self.occurency_list = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        t = 0
        
        for i in self.word_list:
            for y in i:
                t += 1
                self.occurency_list[y] += 1

        for i in self.occurency_list:
            self.occurency_list[i] = self.occurency_list[i] * 100 / t


    def compute_word_frequency_value(self):
        """
        For each word, we compute they frequency value by adding the frequency of each letter
        With it, we determine which word has the most probability for being our answer
        We output this word
        """
        word_occurency_list = [0] * len(self.custom_wordlist)
        for i in range(len(self.custom_wordlist)):
            for y in range(5):
                word_occurency_list[i] += self.occurency_list[self.custom_wordlist[i][y]]

        return self.custom_wordlist[word_occurency_list.index(max(word_occurency_list))]


    def selection_letters(self):
        """ Here we're selecting the accepted letters for the custom wordlist"""
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        selected_letters = [alphabet * 5]   #for each letter of the word to guess, we're selecting the accepted letters

        for i in range(5):
            if self.result[i] == 'w':
                for y in range(5):
                    selected_letters[y].remove(self.guess[i])

            elif self.result[i] == 'c':
                selected_letters[i] = self.word_to_guess[i]
                

            elif self.result[i] == 'm':
                selected_letters.append(alphabet).remove(self.guess[i])


    def build_custom_wordlist(self):
        """ we selecting all the word which contains the selected letter. At the end we remove all the words with several same letters to improve the chance of finding a letter from the word to guess"""
        self.selection_letters()


    def solver(self):
        self.build_custom_wordlist()
        self.guess = self.compute_word_frequency_value()
        self.custom_wordlist.remove(self.guess)
        self.compare()


    def play(self):
        c = 1

        while c < 7:
            self.solver()
            print (f"Turn {c}:\n   Guess: {self.guess}\n   Result: {self.result}\n   Wordlist len: {len(self.word_list)}\n")
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