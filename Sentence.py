import spacy
from Question import Question
from QkDictionary import QkDictionary
import random

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

    # Brute force detections based on NOUNs
    def find_subjects(self):
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
            if token.pos_ == 'PROPN':
                self.subjects.append(token.text)
                #print ("Subject = " + token.text)

    # Detections based on named entity detection
    def find_subjects_ent(self):
        for ent in self.doc.ents:
            self.subjects.append(ent.text)

    # Remove subjects that aren't desirable
    def clean_subjects(self):
        for subject in self.subjects:
            if (subject.lower() == self.article.title.lower() or \
                    subject.lower() in (name.lower() for name in self.article.title.split())) or \
                    self.article.is_subject_used(subject): # Try to avoid repeating the same answer appearing in different questions
                self.subjects.remove(subject)
   

    def parse(self):
        #print('Parsing content in [{}]'.format(self.text))
        self.doc = self.nlp(self.text)

        self.find_subjects_ent()
        self.clean_subjects()

        if self.subjects:   # not empty
            #print('Simple sentence [{}]'.format(self.text))
            #print('subjects:{}'.format(self.subjects))

            # Create a fill in blanks type of question
            # for now, just use one subject randomly from the list
            subject_text = random.choice(self.subjects)
            question_str = self.text.replace(subject_text, '______', 1)  # replace only the first occurrence

            # Exclude the title from answer choices
            exclude_list = self.article.title.split()
            choices = self.article.dictionary.get_similar(subject_text, exclude_list, 3)
            self.question = Question(question_str, subject_text, choices)
            #print(self.question)

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return "Sentence({})".format(self.text)


