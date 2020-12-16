import spacy

class Sentence:
    """
    Base Sentence type

    """

    def __init__(self, nlpdoc):
        self.nlpdoc = nlpdoc

    def parse(self):
        print('==Parsing content in [{}]'.format(self.nlpdoc))

        for token in self.nlpdoc:
            print(token.text, token.pos_, token.dep_)

    def __str__(self):
        return str(self.nlpdoc)

    def __repr__(self):
        return "Sentence({})".format(self.nlpdoc)


