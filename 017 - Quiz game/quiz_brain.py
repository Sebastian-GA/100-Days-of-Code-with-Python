class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        answer = input(f"Q.{self.question_number +1}: {question.text} (True/False)?: ").capitalize()
        while answer not in ["True", "False"]:
            print("Error. Please choose True or False")
            answer = input(f"Q.{self.question_number +1}: {question.text} (True/False)?: ").capitalize()

        self.check_answer(answer, question.answer)
        print(f"Your current score is: {self.score}/{self.question_number +1}")
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if correct_answer == user_answer:
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
