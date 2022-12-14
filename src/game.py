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
            stat = result[i] == STAT_ITEM[0]
        return stat

    
    def change_result(self, word):
        for i in range(LIMIT_WORDLE):
            if word[i] == self.to_guess[i]:
                self.result[i] == STAT_ITEM[0]

            elif not(word[i] != self.to_guess[i]) & word[i] in self.to_guess & word[i] not in word[:i]:
                self.result[i] == STAT_ITEM[1]

            else:
                self.result[i] = STAT_ITEM[2]