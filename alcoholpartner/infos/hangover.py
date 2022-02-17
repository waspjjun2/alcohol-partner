"""
숙취해소법을 알려줍니다.

"""
import random

from alcoholpartner import resource
from alcoholpartner.info import InfoProvider
from alcoholpartner.message import Message

TEXTS = [
    resource.path_for('hangover/숙취해소1.txt'),
    resource.path_for('hangover/숙취해소2.txt'),
    resource.path_for('hangover/숙취해소3.txt'),
    resource.path_for('hangover/숙취해소4.txt'),
    resource.path_for('hangover/숙취해소5.txt'),
]


class Hangover(InfoProvider):
    def extract_args(self, text):
        return True

    def get_info(self, args):
        return random.choice(TEXTS)

    def info_to_message(self, args, info):
        with open(info) as f:
            return Message(
                text=f.read(),
            )
