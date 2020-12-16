import spacy

class Article:
    """
    Base Article type

    """

    def __init__(self, title):
        self.title = title
        self.content = ''
        self.sentences = []
        print('Loading spacy data set en small')
        self.nlp = spacy.load("en_core_web_sm")

    def set_content(self, content):
        self.content = content

    def parse(self):
        print('Parsing content in ' + self.title)
        self.doc = self.nlp(self.content)

        for sent in self.doc.sents:
            self.sentences.append(sent)
        print ('Number of sentences in {}={}'.format(self.title, str(len(self.sentences))))
        print ('First sentence [ {} ]'.format(self.sentences[0]))

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return "Article({})".format(self.title)


