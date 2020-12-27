import spacy
from Question import Question


class Sentence:
    """
    Base Sentence type

    """

    def __init__(self, nlp, text, title):
        self.nlp = nlp
        self.text = text
        self.title = title
        self.subjects = []

        # A sentence is marked as  simple based on some criteria
        # that helps it to be converted to a simple question
        # of fill-in-the blank type of format
        self.is_simple = False

    def parse(self):
        #print('Parsing content in [{}]'.format(self.text))
        self.doc = self.nlp(self.text)

        for token in self.doc:
            if token.pos_ == 'PROPN' and token.text != self.title:
                self.subjects.append([token.text, token.i])
                self.is_simple = True
        
        if self.subjects:   # not empty
            #print('Simple sentence [{}]'.format(self.text))
            #print('subjects:{}'.format(self.subjects))

            # Create a fill in blanks type of question
            # for now, just use the first subject
            subject_text = self.subjects[0][0]
            subject_idx = self.subjects[0][1]
            question_str = self.text.replace(subject_text, '______')

            self.question = Question(question_str, [subject_text, 'ans 2', 'ans 3'], 0)
            print(self.question)

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return "Sentence({})".format(self.text)


