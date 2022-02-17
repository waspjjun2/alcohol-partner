"""
구구단 퀴즈입니다.

"""
import datetime
import random
import re

from alcoholpartner.quiz import Quiz, QuizManager
from alcoholpartner.message import Message


class GugudanQuiz(Quiz):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def analyze_text(self, text):
        match = re.match(r'\d+', text.strip())
        if not match:
            return None
        return int(match.group())

    def check_answer(self, answer):
        expected = self.left * self.right
        return answer == expected

    def lifespan(self):
        return datetime.timedelta(seconds=30)


class Gugudan(QuizManager):
    def generate_quiz(self):
        left = random.randint(2, 9)
        right = random.randint(1, 9)
        return GugudanQuiz(
            left=left,
            right=right,
        )

    def quiz_to_message(self, quiz) -> Message:
        return Message("%d x %d = ?" % (quiz.left, quiz.right))
