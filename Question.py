class Question:
    """
    Base question type

    """

    def __init__(self, question_str, answer, alternates):
        self.question_str = question_str
        self.answer = answer
        self.alternates = alternates
        self.answer_idx = 0

    def __str__(self):
        ret_str = ''
        ret_str += 'Q. ' + self.question_str + '\n'
        ret_str += 'a. ' + self.answer + '\n'

        for alternate in self.alternates:
            ret_str += 'a. ' + alternate + '\n'
        return ret_str

    def __repr__(self):
        return "Question({})".format(self.question_str)


