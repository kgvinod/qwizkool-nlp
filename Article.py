import spacy
from Sentence import Sentence
from QkDictionary import QkDictionary

class Article:
    """
    Base Article type

    """

    def __init__(self, title):
        self.title = title
        self.content = ''
        self.sentences = []
        self.model = "en_core_web_md"

        print('Loading spacy model' + self.model)
        self.nlp = spacy.load(self.model)

    def set_content(self, content):
        self.content = content

    def parse(self):
        print('Parsing content in ' + self.title)
        self.doc = self.nlp(self.content)
        self.dictionary = QkDictionary(self.get_all_nouns())

        print('Generating sentences in ' + self.title)
        for sent in self.doc.sents:
            self.sentences.append(Sentence(self.nlp, sent.text, self))
        
        print ('Number of sentences in {}={}'.format(self.title, str(len(self.sentences))))
        print ('First sentence [ {} ]'.format(self.sentences[0]))

        print('Parsing sentences in ' + self.title)
        for sentences in self.sentences:
            sentences.parse()

    def get_all_nouns(self):
        nouns = []
        for token in self.doc:
            if token.pos_ == 'PROPN':
                nouns.append(token.text)           
        return nouns        

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return "Article({})".format(self.title)


