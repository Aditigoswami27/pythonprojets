from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    item = Question(question_text,question_answer)
    question_bank.append(item)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz.")
print(f"your final score is {quiz.score}/{len(question_bank)}")

