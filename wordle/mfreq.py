from copy import deepcopy

""" Specific attributes from Wordlist and Frequency_letter are specified like this: self.attributes_data """

class Frequency_letter():
    def __init__(self, wordlist_obj):
        """ 
        A single function for computing the letters occurency in the wordlist and the occurency of all the letters in every positions
        We form the alphabet_data like this: 
            self.alphabet_data = {'a': [freq_wordlist, [freq_pos1, freq_pos2, freq_pos2, freq_pos3, freq_pos4, freq_pos5]]}

        The strategy if to compute the frenquency of a letter in a certain position
        
        """

        self.alphabet_data = {'a': [0, [0, 0, 0, 0, 0]], 'b': [0, [0, 0, 0, 0, 0]], 'c': [0, [0, 0, 0, 0, 0]], 'd': [0, [0, 0, 0, 0, 0]], 'e': [0, [0, 0, 0, 0, 0]], 'f': [0, [0, 0, 0, 0, 0]], 'g': [0, [0, 0, 0, 0, 0]], 'h': [0, [0, 0, 0, 0, 0]], 'i': [0, [0, 0, 0, 0, 0]], 'j': [0, [0, 0, 0, 0, 0]], 'k': [0, [0, 0, 0, 0, 0]], 'l': [0, [0, 0, 0, 0, 0]], 'm': [0, [0, 0, 0, 0, 0]], 'n': [0, [0, 0, 0, 0, 0]], 'o': [0, [0, 0, 0, 0, 0]], 'p': [0, [0, 0, 0, 0, 0]], 'q': [0, [0, 0, 0, 0, 0]], 'r': [0, [0, 0, 0, 0, 0]], 's': [0, [0, 0, 0, 0, 0]], 't': [0, [0, 0, 0, 0, 0]], 'u': [0, [0, 0, 0, 0, 0]], 'v': [0, [0, 0, 0, 0, 0]], 'w': [0, [0, 0, 0, 0, 0]], 'x': [0, [0, 0, 0, 0, 0]], 'y': [0, [0, 0, 0, 0, 0]], 'z': [0, [0, 0, 0, 0, 0]]}

        for i in wordlist_obj.wordlist:
            for y in range(5):
                self.alphabet_data[i[y]][0] += 1   #wordlist occurency
                self.alphabet_data[i[y]][1][y] += 1


    def get_most_probable_word(self):
        for freq, pos_freq in self.alphabet_data.items():
            print (freq, pos_freq[0])

    
    def get_letter_in_pos(self):
        pass