import spacy
from Sentence import Sentence
from QkDictionary import QkDictionary

class Article:
    """
    Base Article type

    """

    def __init__(self, title, ctx):
        self.title = title
        self.content = ''
        self.sentences = []
        self.nlp = ctx.nlp

    def set_content(self, content):
        self.content = content

    def parse(self):
        print('Parsing content about ' + self.title)
        self.doc = self.nlp(self.content)
        self.dictionary = QkDictionary(self.get_all_nouns())

        for count, sent in enumerate(self.doc.sents, start=1):
            print('Generating sentences: ' + str(count), end='\r')
            self.sentences.append(Sentence(sent.text, self))              
        print()

        #print ('Lines of information collected = {}'.format(str(len(self.sentences))))

        for count, sentence in enumerate(self.sentences, start=1):
            print('Parsing Sentence: ' + str(count), end='\r')
            sentence.parse()    
        print()

        print ('\n' + self.title + ': [ {} ]'.format(self.sentences[0]))

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


