import json



class Question:
    """
    Create a quiz model by using the Question class to initialize new question objects,
    the new question objects will possess the question_text, answer_options and 
    correct_answer attributes
    """

    def __init__(self, question_text, answer_options, correct_answer):
        self.question_text = question_text
        self.answer_options = answer_options
        self.correct_answer = correct_answer
    