"""
숙취해소법을 알려줍니다.

"""
import random

from alcoholpartner import resource
from alcoholpartner.info import InfoProvider
from alcoholpartner.message import Message

TEXTS = [
    resource.path_for('remedy/해장1.txt'),
    resource.path_for('remedy/해장2.txt'),
    resource.path_for('remedy/해장3.txt'),
    resource.path_for('remedy/해장4.txt'),
    resource.path_for('remedy/해장5.txt'),
]


class Remedy(InfoProvider):
    def extract_args(self, text):
        return True

    def get_info(self, args):
        return random.choice(TEXTS)

    def info_to_message(self, args, info):
        with open(info) as f:
            return Message(
                text=f.read(),
            )
