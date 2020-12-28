import random

class QkDictionary:
    """
    Provide dictionary, thesaurus utilities

    """

    def __init__(self, vocab):
        self.vocab = vocab

    def get_synonym(self, word, count):
        pass

    def get_antonym(self, word, count):
        pass

    # These are not synonyms. These are words from
    # similar category of words
    # Similar word examples:
    #  USA : [Australia, India, New Zealand] 
    #  President : [Prime Minister, Queen, Governor]
    #  Car : [Bus, Truck, Motorcycle]
    def get_similar(self, word, count):
        ret_list = []
        for i in range(count):
            rnd_idx = random.randrange(len(self.vocab))
            ret_list.append(self.vocab[rnd_idx])
        return ret_list    
