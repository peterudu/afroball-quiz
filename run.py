import json
import os
import sys
import random


class Question:
    """
    Create a quiz model by using the Question class to initialize new question
    objects, the new question objects will possess the text, options and
    solution attributes
    """

    def __init__(self, text, options, solution):
        self.text = text
        self.options = options
        self.solution = solution

    def accurate(self, answer):
        return self.solution == answer


class Questionsbank:
    """
    Use Questionsbank class with __init__() method to initialize a list of new
    objects which will contain questions text, options and solution details
    collected from the json file
    """

    def __init__(self):
        self.questions = []
        self.score = 0

    # append empty questions list with question details from imported json file
    def load_questions_data(self, pathname):
        with open(pathname, "r") as file:
            details = json.load(file)
            for q_detail in details:
                question = Question(
                    q_detail["text"], q_detail["options"], q_detail["solution"]
                )
                self.questions.append(question)

    # reset the creation of new questions and start the process all over again
    def reset(self):
        self.score = 0

    # display each question text based on index. Options index starts from 1
    def print_question(self, index, question):
        print("Question {}: {}\n".format(index, question.text))
        for option_index, option in enumerate(question.options, start=1):
            print("   {}. {}\n".format(option_index, option))
        print()

    # interracts with the user and ask for their answer input
    def get_user_choice(self, options_index):
        while True:
            try:
                answer = int(input("Give your answer:\n"))
                if 1 <= answer <= options_index:
                    return answer
                else:
                    print("Your input is invalid. Enter a valid answer.")
            except ValueError:
                print("Your input is invalid. Please enter a number value")

    # Function randomly selects a set of 7 questions for a quiz session and
    # increases score if users answer is correct solution
    def start_quiz(self):
        self.score = 0
        num_of_selected_questions = min(7, len(self.questions))

        mix_questions = random.sample(
            self.questions, num_of_selected_questions)

        for index, question in enumerate(mix_questions, start=1):
            self.print_question(index, question)
            answer = self.get_user_choice(len(question.options))
            if question.accurate(answer):
                self.score += 1
                print("Correct!\n")
            else:
                print("Wrong!\n")
        self.show_results(num_of_selected_questions)

    # Displays a end of the quiz statement and a overall result statement
    # at end of every quiz session.
    def show_results(self, num_of_selected_questions):
        print("End of afroBall quiz!")

        user_score_in_percent = (self.score / num_of_selected_questions) * 100
        result = "You scored: {} from {} points which is ({:.2f}%)".format(
            self.score, num_of_selected_questions, user_score_in_percent)

        print("==============================================")
        print(result)
        print("==============================================")


def clean_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


# Function to run the quiz
def main():
    while True:
        q = Questionsbank()
        q.load_questions_data("caf_questions.json")

        print(r"""        __         ___       _ _    ___       _
  __ _ / _|_ _ ___| _ ) __ _| | |  / _ \ _  _(_)___
 / _` |  _| '_/ _ \ _ \/ _` | | | | (_) | || | |_ /
 \__,_|_| |_| \___/___/\__,_|_|_|  \__\_\\_,_|_/__|
                                                   """)

        name = input("Enter your name: ")
        print("Hello %s Welcome to afroBall Quiz...." % (name))
        print("-------------------------------------------------------------")
        q.start_quiz()

        replay_quiz = input("Do you want to do the quiz again? (yes/no):\n")
        if (replay_quiz).lower() != "yes":
            print("Thank you for doing the quiz!")
            break
        else:
            print("Enjoy the quiz!\n")
            clean_screen()


if __name__ == "__main__":
    main()
