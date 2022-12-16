""" The actual games of Wordle 

correct: 'c'
correct but wrong place: 'm'
incorrect: 'i'
"""

LIMIT_WORDLE = 5
STAT_ITEM = ['c', 'm', 'i']


class Wordle:
    def __init__(self, wordlist) -> None:
        self.to_guess = wordlist.get_wordle()
        self.result = ['', '', '', '', '']
        
    
    def is_winning(self):
        stat = 0

        for i in range(LIMIT_WORDLE):
            stat = self.result[i] == STAT_ITEM[0]
        return stat

    
    def change_result(self, word, word_to_guess):
        """ Rules: for each letters
        - if the guessed letter is at the right place: 'c'

        - if the guessed letter at in the word but wrong place: 'm'
        - but if guessed word had twice the same letter and the wordle only have it once: only the first will get the 'm', else: 'i'
        
        - if the guessed letter appear nowhere: 'i'

        """
        for i in range(LIMIT_WORDLE):
            if word[i] == word_to_guess[i]:
                self.result[i] = STAT_ITEM[0]
                word_to_guess[i] = ""
            

            elif (word[i] != word_to_guess[i]) & (word[i] in word_to_guess):
                self.result[i] = STAT_ITEM[1]

            else:
                self.result[i] = STAT_ITEM[2]
        