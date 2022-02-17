"""
Bot의 전체 사이클을 구현하는 코드입니다.

텔레그램과 소통하며 명령어, 텍스트를 입력받아 메시지를 보낸 사용자의 현재
상태에 따라 올바른 명령을 수행합니다.

"""
import datetime
import random

import telegram
from telegram.ext import CommandHandler, RegexHandler, Updater

from . import texts
from .info_dispatcher import dispatch_info
from .level import Level
from .state import STATUS_PENDING_QUIZ, State
from .timer import AutoIncrementTimer, QuizTimer


class AlcoholPartner(object):
    def __init__(self, token):
        super().__init__()
        self.states = {}
        self.token = token
        self._next_session_id = 0

    def state_for(self, update: telegram.Update):
        if update.effective_user is None:
            return None
        if update.effective_user.id in self.states:
            state = self.states[update.effective_user.id]
            state.chat_id = update.message.chat_id
        else:
            state = State(
                user_id=update.effective_user.id,
                chat_id=update.message.chat_id,
                session_id=self.next_session_id(),
            )
            self.states[state.user_id] = state
        return state

    def start(self):
        print("Starting alcohol friend")
        updater = Updater(token=self.token)
        dispatcher = updater.dispatcher

        commands = {
            'start': self.as_telegram_command(self.start_command),
            'stop': self.as_telegram_command(self.stop_command),
        }

        for name, callback in commands.items():
            handler = CommandHandler(name, callback, pass_args=True)
            dispatcher.add_handler(handler)

        text_handler = RegexHandler(r'.*', self.handle_text)
        dispatcher.add_handler(text_handler)

        updater.start_polling()

    def handle_text(self, bot: telegram.Bot, update: telegram.Update):
        state = self.state_for(update)
        if state is None:
            print("Text from unknown user: " + update.message.text)
        if state.status() == STATUS_PENDING_QUIZ:
            # Expect quiz answer
            self.check_quiz_answer(bot, state, update)
        else:
            # Expect question
            info_provider = dispatch_info(state, update)
            if info_provider is None:
                self.send_unknown(bot, state)
                return
            args = info_provider.extract_args(update.message.text)
            if args is None:
                self.send_unknown(bot, state)
                return
            info = info_provider.get_info(args)
            message = info_provider.info_to_message(args, info)
            message.send(bot, state.chat_id)

    def send_unknown(self, bot: telegram.Bot, state: State):
        message = random.choice(texts.INFO_CANT_UNDERSTAND_MESSAGES)
        message.send(bot, state.chat_id)

    def check_quiz_answer(self, bot: telegram.Bot, state: State,
                          update: telegram.Update):
        quiz = state.pending_quiz
        answer = quiz.analyze_text(update.message.text)
        if answer is None:
            self.handle_wrong_answer(bot, state)
        elif state.pending_quiz.check_answer(answer):
            self.handle_right_answer(bot, state)
        else:
            self.handle_wrong_answer(bot, state)
        self.schedule_next_quiz(bot, state)

    def handle_wrong_answer(self, bot: telegram.Bot, state: State):
        increment = state.get_score_increment()
        message = random.choice(texts.QUIZ_WRONG_ANSWER_MESSAGES)
        message.send(bot, state.chat_id)
        state.increase_score(increment, bot)

    def handle_right_answer(self, bot: telegram.Bot, state: State):
        decrement = 5
        message = random.choice(texts.QUIZ_RIGHT_ANSWER_MESSAGES)
        message.send(bot, state.chat_id)
        state.decrease_score(decrement, bot)

    def schedule_next_quiz(self, bot, state):
        delay = self.get_quiz_delay(state)
        timer = QuizTimer(bot, state, delay, session_id=state.session_id)
        timer.start()

    def get_quiz_delay(self, state: State):
        level = state.level()
        if level == Level.LEVEL1:
            # return datetime.timedelta(minutes=30).total_seconds()
            # return datetime.timedelta(seconds=30).total_seconds()
            return datetime.timedelta(seconds=5).total_seconds()
        elif level == Level.LEVEL2:
            # return datetime.timedelta(minutes=20).total_seconds()
            # return datetime.timedelta(seconds=20).total_seconds()
            return datetime.timedelta(seconds=5).total_seconds()
        elif level == Level.LEVEL3:
            # return datetime.timedelta(minutes=10).total_seconds()
            # return datetime.timedelta(seconds=10).total_seconds()
            return datetime.timedelta(seconds=5).total_seconds()
        elif level == Level.LEVEL4:
            # return datetime.timedelta(minutes=5).total_seconds()
            # return datetime.timedelta(seconds=5).total_seconds()
            return datetime.timedelta(seconds=5).total_seconds()
        else:
            # return datetime.timedelta(minutes=5).total_seconds()
            # return datetime.timedelta(seconds=5).total_seconds()
            return datetime.timedelta(seconds=5).total_seconds()

    def start_command(self, bot: telegram.Bot, state: State, args):
        if state.started:
            # Don't ruin the state
            texts.SESSION_ALREADY_STARTED.send(bot, state.chat_id)
            return
        state.start()

        self.schedule_next_quiz(bot, state)
        timer = AutoIncrementTimer(state, bot, state.session_id)
        timer.start()

        texts.SESSION_STARTED.send(bot, state.chat_id)

    def stop_command(self, bot: telegram.Bot, state: State, args):
        if not state.started:
            # Don't ruin the state
            texts.SESSION_ALREADY_STOPPED.send(bot, state.chat_id)
            return
        state.stop()
        state.session_id = self.next_session_id()

        texts.SESSION_STOPPED.send(bot, state.chat_id)

    def as_telegram_command(self, callback):
        def wrapper(bot, update, args):
            state = self.state_for(update)
            if state is None:
                print("Command from unknown user")
                return
            callback(bot, state, args)
        return wrapper

    def next_session_id(self):
        session_id = self._next_session_id
        self._next_session_id += 1
        return session_id
