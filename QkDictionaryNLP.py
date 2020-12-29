import random
from QkDictionary import QkDictionary

class QkDictionaryNLP(QkDictionary):
    """
    Provide dictionary, thesaurus utilities

    """

    def __init__(self, vocab, ctx):
        QkDictionary.__init__(self, vocab)
        self.nlp = ctx.nlp

    def get_similar(self, word, exclude_list, count):
        ret_list = []

        # Try continously until we get enough
        num_tries = len(self.vocab) * 10
        for _ in range(num_tries):
            rnd_idx = random.randrange(len(self.vocab))
            choice_word = self.vocab[rnd_idx]

            if not self.is_english_chars(choice_word):
                continue

            # Skip small words    
            if len(choice_word) <=2:
                continue 

            # We don't need one that's same as the input word
            if choice_word.lower() == word.lower():
                continue

            # We don't need anything from the exclude list
            if choice_word.lower() in (name.lower() for name in exclude_list):
                continue    

            # Exclude really small words
            if len(choice_word) <=2 :
                continue
            
            # Skip duplicates
            if choice_word.lower() in (name.lower() for name in ret_list):
                continue  

            ret_list.append(self.vocab[rnd_idx])
            if len(ret_list) >= count:
                break

        return ret_list    

