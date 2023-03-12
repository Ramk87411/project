from data import question_data
from question import Question
from quiz import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # new question 0bject and saved inn to question bank
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")
