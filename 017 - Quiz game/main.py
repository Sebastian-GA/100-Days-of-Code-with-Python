from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from random import shuffle

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(quiz.questions_list)}")
