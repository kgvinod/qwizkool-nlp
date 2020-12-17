import spacy

class Sentence:
    """
    Base Sentence type

    """

    def __init__(self, nlp, text):
        self.nlp = nlp
        self.text = text
        self.subjects = []
        self.objects = []

    def parse(self):
        print('Parsing content in [{}]'.format(self.text))
        self.doc = self.nlp(self.text)

        for token in self.doc:
            if token.dep_ == 'nsubj':
                self.subjects.append(token.text)
            if token.dep_ == 'dobj':
                self.objects.append(token.text)
        
        print(self.subjects, self.objects)

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return "Sentence({})".format(self.text)


