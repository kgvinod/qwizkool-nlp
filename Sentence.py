import spacy
from Question import Question

class Sentence:
    """
    Base Sentence type

    """

    def __init__(self, nlp, text, article):
        self.nlp = nlp
        self.text = text
        self.article = article
        self.subjects = []
        self.question = None

        # A sentence is marked as  simple based on some criteria
        # that helps it to be converted to a simple question
        # of fill-in-the blank type of format
        self.is_simple = False

    def parse(self):
        #print('Parsing content in [{}]'.format(self.text))
        self.doc = self.nlp(self.text)

        # Start simple sentence detection
        # If the first word is a pronoun, it is most likely
        # a continuation sensence. So skip it.
        if self.doc[0].pos_ == 'PRON':
            return

        # Absence of a verb indicates a non well formed simple sentence
        for token in self.doc:
            if token.pos_ == 'VERB':
                break
        else:
            return

        # Pick the candidates for 'answer' to a question form of
        # the sentence
        for token in self.doc:
            if token.pos_ == 'PROPN' and token.text.lower() != self.article.title.lower() and token.text.lower() not in (name.lower() for name in self.article.title.split()):
                self.subjects.append([token.text, token.i])
                self.is_simple = True
        
        if self.subjects:   # not empty
            #print('Simple sentence [{}]'.format(self.text))
            #print('subjects:{}'.format(self.subjects))

            # Create a fill in blanks type of question
            # for now, just use the first subject
            subject_text = self.subjects[0][0]
            question_str = self.text.replace(subject_text, '______')

            # Exclude the title from anwer choices
            exclude_list = self.article.title.split()
            choices = self.article.dictionary.get_similar(subject_text, exclude_list, 3)
            self.question = Question(question_str, subject_text, choices)
            #print(self.question)

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return "Sentence({})".format(self.text)


