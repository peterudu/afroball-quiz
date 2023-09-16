import json
import os
import sys
import random


class Question:
    """
    Create a quiz model by using the Question class to initialize new question objects,
    the new question objects will possess the text, options and solution attributes
    """

    def __init__(self, text, options, solution):
        self.text = text
        self.options = options
        self.solution = solution

    def accurate(self, answer):
        return self.solution == answer
    

class Questionsbank:
    """
    Use Questionsbank class to produce a list of new objects which will contain questions text,
    options and solution details collected from the json file
    """

    def __init__(self):
        self.questions = []
        self.score = 0

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
                answer = int(input("Give your answer: "))
                if 1 <= answer <= options_index:
                    return answer
                else:
                    print("Your input is invalid. Enter a valid answer.")
            except ValueError:
                print("Your input is invalid. Please enter a number value")        

    def start_quiz(self):
        self.score = 0
        num_of_selected_questions = min(7, len(self.questions))

        mix_questions = random.sample(self.questions, num_of_selected_questions)

        for index, question in enumerate(mix_questions, start=1):
            self.print_question(index, question)
            answer = self.get_user_choice(len(question.options))
            if question.accurate(answer):
                self.score += 1
                print("Correct!\n")
            else:
                print("Wrong!\n")
        self.show_results(num_of_selected_questions)

    def show_results(self, num_of_selected_questions):
        print("End of afroBall quiz!")

        user_score_in_percent = (self.score / num_of_selected_questions) * 100
        results_info_text = "You scored in: {} out of {} questions which makes ({:.2f}%)".format(
            self.score, num_of_selected_questions, user_score_in_percent)
        print(results_info_text)


def clean_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

def main():
    while True:
        q = Questionsbank()
        q.load_questions_data("caf_questions.json")

        print("Welcome to afroBall Quiz.")
        q.start_quiz()



if __name__ == "__main__":      
    main()
