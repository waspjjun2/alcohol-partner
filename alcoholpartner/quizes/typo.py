import datetime

import random
from alcoholpartner import texts, image
from alcoholpartner.quiz import Quiz, QuizManager
from alcoholpartner.message import Message

ITEMS = [
    (
        image.path_for('typo/a.png'),
        "저기있는 저 분은 박 법학박사이고, 여기있는 이 분은 백법학박사이다."
    ),
    (
        image.path_for('typo/b.png'),
        "검찰청 쇠철창살은 새쇠철창살이냐 헌쇠철창살이냐."
    ),
    (
        image.path_for('typo/c.png'),
        "한양양장점 옆 한영양점점, 한영양장점 옆 한양양장점."
    ),
    (
        image.path_for('typo/d.png'),
        "저기있는 말말뚝이 말 맬만한 말말뚝이냐 말 못맬 만한 말말뚝이냐."
    ),
    (
        image.path_for('typo/e.png'),
        "옆집팥죽은 붉은 팥 팥죽이고, 뒷집 콩죽은 검은콩 콩죽이다."
    ),
    (
        image.path_for('typo/f.png'),
        "박범복군은 밤벚꽃놀이를 가고 방범복양은 낮벚꽃놀이를 간다."
    ),
    (
        image.path_for('typo/g.png'),
        "내가 그린 기린 그림은 잘 그린 기린 그림이고, 네가 그린 기린 그림은 못 그린 기린 그림이다."
    ),
    (
        image.path_for('typo/h.png'),
        "한양 양장점 옆 한영 양장점"
    ),
    (
        image.path_for('typo/i.png'),
        "신인 샹송 가수의 신춘 샹송 쇼"
    ),
    (
        image.path_for('typo/j.png'),
        "고려고 교복은 고급교복이고 고려고 교복은 고급원단을 사용했다."
    ),
    (
        image.path_for('typo/k.png'),
        "상표 붙인 큰 깡통은 깐 깡통인가? 안 깐 깡통인가?"
    ),
    (
        image.path_for('typo/l.png'),
        ("앞 집 팥죽은 붉은 팥 풋팥죽이고 , 뒷집 콩죽은 햇콩단콩 콩죽,우리집 깨죽은 검은깨 깨죽인데 사람들은 햇콩 단콩 콩죽 "
         "깨죽 죽먹기를 싫어하더라.")
    ),
]


class TypoQuiz(Quiz):
    def __init__(self, image, text):
        super().__init__()
        self.image = image
        self.text = text

    def analyze_text(self, text: str):
        return text.strip().rstrip('.')

    def check_answer(self, answer):
        return self.text.strip().rstrip('.') == answer

    def lifespan(self):
        return datetime.timedelta(minutes=3)


class Typo(QuizManager):
    def generate_quiz(self):
        image, text = random.choice(ITEMS)
        return TypoQuiz(image=image, text=text)

    def quiz_to_message(self, quiz) -> Message:
        return Message(
            text=texts.QUIZ_TYPO_TEXT,
            images=[
                quiz.image,
            ]
        )
