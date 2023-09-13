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
    

class Questionsbank:
    """
    Use Questionsbank class to produce a list of new objects which will contain questions text
    and answer options data collected from the json file
    """

    def __init__(self):
        self.questions = []


