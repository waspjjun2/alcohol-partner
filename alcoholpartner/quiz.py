"""
퀴즈 생성기와 퀴즈를 정의하는 코드입니다.
"""

import datetime

from .message import Message


class Quiz(object):
    def __init__(self):
        super().__init__()
        self.created_at = datetime.datetime.now()

    def analyze_text(self, text):
        pass

    def check_answer(self, answer):
        pass

    def lifespan(self) -> datetime.timedelta:
        pass

    def expired_at(self) -> datetime.datetime:
        return self.created_at + self.lifespan()

    def is_expired(self) -> bool:
        return datetime.datetime.now() > self.expired_at()


class QuizManager(object):
    def generate_quiz(self):
        pass

    def quiz_to_message(self) -> Message:
        pass
