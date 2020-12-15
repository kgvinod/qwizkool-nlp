class Question:
    """
    Base question type

    """

    def __init__(self, question_str):
        self.question_str = question_str

    def __str__(self):
        return str(self.question_str)

    def __repr__(self):
        return "Question({})".format(self.question_str)


