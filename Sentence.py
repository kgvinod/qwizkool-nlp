import spacy
from Question import Question
from QkDictionary import QkDictionary

class Sentence:
    """
    Base Sentence type

    """

    def __init__(self, text, article):
        self.nlp = article.nlp
        self.text = text
        self.article = article
        self.subjects = []
        self.question = None

    def parse(self):
        #print('Parsing content in [{}]'.format(self.text))
        self.doc = self.nlp(self.text)

        # Skip sentences with non english characters
        if not QkDictionary().is_english_chars(self.text):
            return
        
        # Start simple sentence detection
        # If the first word is a pronoun, it is most likely
        # a continuation sentence. So skip it.
        if self.doc[0].pos_ == 'PRON':
            return

        # Absence of a verb indicates a non simple sentence
        for token in self.doc:
            if token.pos_ == 'VERB':
                break
        else:
            return

        # Pick the candidates for 'answer' words
        for token in self.doc:
            if (token.pos_ == 'PROPN' and \
                    token.text.lower() != self.article.title.lower() and \
                    token.text.lower() not in (name.lower() for name in self.article.title.split())) and \
                    not self.article.is_subject_used(token.text): # Try to avoid repeating the same answer appearing in different questions
                self.subjects.append(token.text)
                #print ("Subject = " + token.text)
        
        if self.subjects:   # not empty
            #print('Simple sentence [{}]'.format(self.text))
            #print('subjects:{}'.format(self.subjects))

            # Create a fill in blanks type of question
            # for now, just use the first subject
            subject_text = self.subjects[0]
            question_str = self.text.replace(subject_text, '______')

            # Exclude the title from answer choices
            exclude_list = self.article.title.split()
            choices = self.article.dictionary.get_similar(subject_text, exclude_list, 3)
            self.question = Question(question_str, subject_text, choices)
            #print(self.question)

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return "Sentence({})".format(self.text)


