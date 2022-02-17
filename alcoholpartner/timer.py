"""
일정 주기로 실행되는 작업들을 정의합니다.
"""

import datetime
import random
import threading

import telegram

from . import texts
from .quiz import Quiz, QuizManager
from .quizes.gugudan import Gugudan
from .quizes.number import Number
from .quizes.typo import Typo
from .state import State

QUIZ_MANAGERS = [
    Gugudan(),
    Typo(),
    Number(),
]


class QuizExpireTimer(object):
    def __init__(self, quiz: Quiz, bot: telegram.Bot, state: State,
                 delay, session_id):
        super().__init__()
        self.quiz = quiz
        self.bot = bot
        self.state = state
        self.delay = delay
        self.session_id = session_id

    def start(self):
        if self.is_valid():
            print("Quiz expire timer Stopped: " + str(self.state.user_id))
            return
        t = threading.Timer(self.delay, self.on_timer)
        t.start()

    def on_timer(self):
        if self.is_valid():
            print("Quiz Stopped: " + str(self.state.user_id))
            return
        if self.state.pending_quiz != self.quiz:
            return
        # Wrong
        self.send_expiration_message()
        self.increase_score()
        self.expire_quiz()

    def send_expiration_message(self):
        message = random.choice(texts.QUIZ_NO_RESPONSE_MESSAGES)
        message.send(self.bot, self.state.chat_id)

    def increase_score(self):
        increment = self.state.get_score_increment()
        self.state.increase_score(increment, self.bot)

    def expire_quiz(self):
        self.state.pending_quiz = None

    def is_valid(self):
        return self.session_id != self.state.session_id


class QuizTimer(object):
    def __init__(self, bot: telegram.Bot, state: State, delay, session_id):
        super().__init__()
        self.bot = bot
        self.state = state
        self.delay = delay
        self.session_id = session_id

    def start(self):
        if self.is_valid():
            print("Quiz Stopped: " + str(self.state.user_id))
            return
        t = threading.Timer(self.delay, self.on_timer)
        t.start()

    def on_timer(self):
        if self.is_valid():
            print("Quiz Stopped: " + str(self.state.user_id))
            return
        quiz_manager = self.choose_quiz_manager()
        quiz = quiz_manager.generate_quiz()
        self.save_quiz(quiz)
        self.send_quiz(quiz_manager, quiz)
        timer = QuizExpireTimer(quiz, self.bot, self.state,
                                quiz.lifespan().total_seconds(),
                                self.state.session_id)
        timer.start()

    def save_quiz(self, quiz):
        self.state.pending_quiz = quiz

    def send_quiz(self, quiz_manager: QuizManager, quiz: Quiz):
        message = quiz_manager.quiz_to_message(quiz)
        message.send(self.bot, self.state.chat_id)

    def choose_quiz_manager(self) -> QuizManager:
        return random.choice(QUIZ_MANAGERS)

    def is_valid(self):
        return self.session_id != self.state.session_id


class AutoIncrementTimer(object):
    def __init__(self, state: State, bot: telegram.Bot, session_id):
        super().__init__()
        self.state = state
        self.bot = bot
        self.session_id = session_id

        # self.interval = datetime.timedelta(minutes=5).total_seconds()
        self.interval = datetime.timedelta(seconds=30).total_seconds()
        self.increment = 5

    def start(self):
        if self.is_valid():
            print("Autoincrement Stopped: " + str(self.state.user_id))
            return
        self.schedule_next()

    def handle_next(self):
        if self.is_valid():
            print("Autoincrement Stopped: " + str(self.state.user_id))
            return
        self.state.increase_score(self.increment, self.bot)
        self.schedule_next()

    def is_valid(self):
        return self.session_id != self.state.session_id

    def schedule_next(self):
        timer = threading.Timer(self.interval, self.handle_next)
        timer.start()
