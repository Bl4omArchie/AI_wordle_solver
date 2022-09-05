""" Specific attributes from Wordlist and Frequency_letter are specified like this: self.attributes_data """


class Wordlist():
    """ Wordlist class for managing the custom wordlist """

    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.len_wordlist = len(self.wordlist)


    def update_custom_wordlist(self):
        pass


    def get_wordlist(self):
        wordlist_return = []
        for word, stat in self.wordlist_data.items():
            if stat == 1:
                wordlist_return.append(word)
        return wordlist_return