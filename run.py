import json
import os
import sys
import random



class Question:
    """
    Create a quiz model by using the Question class to initialize new question objects,
    the new question objects will possess the question_text, answer_options and 
    correct_answer attributes
    """

    def __init__(self, text, options, solution):
        self.text = text
        self.options = options
        self.solution = solution
    

class Questionsbank:

    """
    Use Questionsbank class to produce a list of new objects which will contain questions text
    and answer options details collected from the json file
    """

    def __init__(self):
        self.questions = []


    def load_questions_data(self, pathname):
        with open(pathname, "r") as file:
            details = json.load(file)
            for q_detail in details:
                question = Question(
                    q_detail["text"], q_detail["options"], q_detail["solution"]
                )
                self.questions.append(question)


    def print_question(self, index, question):
        print("Question {}: {}\n".format(index, question.text))
        for option_index, option in enumerate(question.options, start=1):
            print("   {}. {}\n".format(option_index, option))
        print()


    def get_user_choice(self, options_index):
        while True:
            try:
                answer = int(input("Give your answer."))
                if 1 <= answer <= options_index:
                    return answer
                else:
                    print("Your input is invalid. Enter a valid answer.")
            except ValueError:
                print("Your input is invalid. Enter a number value")        


    def start_quiz():
        num_of_selected_questions = min(7, len(self.questions))

        mix_questions = random.sample(self.questions, num_of_selected_questions)


def main():
    

    
main()
