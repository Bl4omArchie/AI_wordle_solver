from src.wordlist import Wordlist


""" The algorithm for auto-solving """

class AI_wordle_solver():
    def __init__(self, wordlist) -> None:
        self.wordlist_obj = wordlist
        self.compute_wordlist_frequency()
        

    def make_guess(self):    #return the guess of the algorithm
        pass


    def compute_wordlist_frequency(self):
        """
        We computing the occurency of each letter in the wordlist
        Then, we the following formula: occurency * 100 / total of all occurency 
        We get the frenquency value of each letter
        """
        self.occurency_list = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        t = 0
        
        for i in self.wordlist_obj.wlist:
            for y in i:
                t += 1
                self.occurency_list[y] += 1

        for i in self.occurency_list:
            self.occurency_list[i] = self.occurency_list[i] * 100 / t