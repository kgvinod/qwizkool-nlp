import random

class Question:
    """
    Base question type

    """

    def __init__(self, question_str, answer, alternates):
        self.question_str = question_str
        self.answer = answer
        self.choices = alternates
        self.answer_idx = random.randrange(len(alternates)+1)
        self.choices.insert(self.answer_idx, answer)

    def generate_question_str(self, question_num):
        ret_str = ''
        ret_str += '\nQ.' + str(question_num) + ' ' + self.question_str + '\n\n'
        choice_num = 1
        for choice in self.choices:
            ret_str += str(choice_num) + '. ' + choice + '\n'
            choice_num += 1
        return ret_str

    def __str__(self):
        ret_str = ''
        ret_str += 'Q. ' + self.question_str + '\n\n'
        choice_num = 1
        for choice in self.choices:
            ret_str += str(choice_num) + '. ' + choice + '\n'
            choice_num += 1
        return ret_str

    def is_correct_answer(self, answer_key):
        return answer_key == self.answer_idx + 1

    def __repr__(self):
        return "Question({})".format(self.question_str)


