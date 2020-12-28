import spacy

class QkContext:
    """
    Context for Qwizkool classes

    """

    def __init__(self, size):

        if size == 'small':
            self.model = "en_core_web_sm"
        elif size == 'medium':
            self.model = "en_core_web_md"
        elif size == 'large':
            self.model = "en_core_web_lg"
        else:
            print ("Unrecognized model size. Choosing small")
            self.model = "en_core_web_sm"

        print('Loading spacy model ' + self.model)
        self.nlp = spacy.load(self.model)



