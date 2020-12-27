class Question:
    """
    Base question type

    """

    def __init__(self, question_str, answers, correct_idx):
        self.question_str = question_str
        self.answers = answers
        self.correct_idx = correct_idx

    def __str__(self):
        ret_str = ''
        ret_str += 'Q. ' + self.question_str + '\n'
        for answer in self.answers:
            ret_str += 'a. ' + answer + '\n'
        return ret_str

    def __repr__(self):
        return "Question({})".format(self.question_str)


