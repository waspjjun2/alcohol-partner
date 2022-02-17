import datetime
import random
import re

from alcoholpartner import image
from alcoholpartner.quiz import Quiz, QuizManager
from alcoholpartner.message import Message


QUIZES = [
    (image.path_for('numbers/picturequiz1.png'), {
        1: 15,
        2: 7,
        3: 14,
        4: 24,
        5: 7,
        6: 12,
        7: 17,
        8: 13,
        9: 12,
    }),
    (image.path_for('numbers/picturequiz2.png'), {
        1: 17,
        2: 12,
        3: 10,
        4: 15,
        5: 11,
        6: 17,
        7: 9,
        8: 17,
        9: 13,
    }),
    (image.path_for('numbers/picturequiz3.png'), {
        1: 20,
        2: 13,
        3: 9,
        4: 10,
        5: 14,
        6: 15,
        7: 14,
        8: 13,
        9: 13,
    })
]


class NumberQuiz(Quiz):
    def __init__(self, image, counts, number):
        super().__init__()
        self.image = image
        self.counts = counts
        self.number = number

    def analyze_text(self, text: str):
        """
        "3개 입니다" -> 3
        "정답은 5개 입니다" -> 5
        "asjdklasjdklasjdklaskl" -> None

        """
        match = re.match(r'\d+', text.strip())
        if match is None:
            return None

        return int(match.group())

    def check_answer(self, answer):
        return answer == self.counts[self.number]

    def lifespan(self):
        return datetime.timedelta(minutes=3)


class Number(QuizManager):
    def generate_quiz(self):
        quiz = random.choice(QUIZES)
        image_path = quiz[0]
        counts = quiz[1]
        number = random.randint(1, 9)
        return NumberQuiz(
            image=image_path,
            counts=counts,
            number=number,
        )

    def quiz_to_message(self, quiz):
        return Message(
            text=f"이 이미지에서 숫자 {quiz.number}는 몇개 있을까요?",
            images=[
                quiz.image,
            ]
        )
