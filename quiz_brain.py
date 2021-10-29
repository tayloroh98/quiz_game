class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(true/false)?")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got the right answer!")
            self.score += 1
        else:
            print("you are wrong")
        print(f"the right answer was {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")