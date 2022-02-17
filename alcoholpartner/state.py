"""
메시지를 보낸 각 사용자의 현재 상태를 나타내는 클래스를 정의하는 코드입니다.

"""
import random

import telegram

from . import texts
from .level import Level, get_level
from .message import Message
from .quiz import Quiz

STATUS_READY = 'READY'
STATUS_STARTED = 'STARTED'
STATUS_PENDING_QUIZ = 'PENDING_QUIZ'


MIN_SCORE = 0
MAX_SCORE = 100


class State(object):
    def __init__(self, user_id, chat_id, session_id):
        super().__init__()
        self.user_id = user_id
        self.chat_id = chat_id
        self.session_id = session_id

        self.started = False
        self.score = 0
        self.pending_quiz: Quiz = None

    def start(self):
        self.started = True
        self.score = 0
        self.pending_quiz = None

    def stop(self):
        self.started = False

    def status(self):
        if not self.started:
            return STATUS_READY
        elif self.pending_quiz:
            return STATUS_PENDING_QUIZ
        else:
            return STATUS_STARTED

    def level(self):
        return get_level(self.score)

    def get_score_increment(self):
        level = self.level()
        if level == Level.LEVEL1:
            return 30
        elif level == Level.LEVEL2:
            return 20
        elif level == Level.LEVEL3:
            return 10
        elif level == Level.LEVEL4:
            return 5
        else:
            return 5

    def increase_score(self, score, bot: telegram.Bot):
        last_score = self.score
        self.score = min(MAX_SCORE, self.score + score)
        self.fire_score_update_event(last_score, self.score, bot)

    def decrease_score(self, score, bot: telegram.Bot):
        last_score = self.score
        self.score = max(MIN_SCORE, self.score - score)
        self.fire_score_update_event(last_score, self.score, bot)

    def fire_score_update_event(self, last_score, new_score,
                                bot: telegram.Bot):
        print(f"User: {self.user_id}, score: {new_score}")
        if get_level(last_score) != get_level(new_score):
            self.send_level_message(get_level(new_score), bot)

    def send_level_message(self, level: Level, bot: telegram.Bot):
        messages = self.get_message_list(level)
        message = random.choice(messages)
        message.send(bot, self.chat_id)

    def get_message_list(self, level: Level) -> Message:
        if level == Level.LEVEL1:
            return texts.LEVEL1_MESSAGES
        elif level == Level.LEVEL2:
            return texts.LEVEL2_MESSAGES
        elif level == Level.LEVEL3:
            return texts.LEVEL3_MESSAGES
        elif level == Level.LEVEL4:
            return texts.LEVEL4_MESSAGES
        else:
            return texts.LEVEL5_MESSAGES
