from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for bank in question_data:
    n_text = bank["question"]
    n_answer = bank["correct_answer"]
    n_question = Question(n_text, n_answer)
    question_bank.append(n_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"your final score is {quiz.score}")
