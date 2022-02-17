"""
숙취해소법을 알려줍니다.

"""
import random

from alcoholpartner import resource
from alcoholpartner.info import InfoProvider
from alcoholpartner.message import Message

TEXTS = [
    resource.path_for('strongliver/술 잘 마시는 법1.txt'),
    resource.path_for('strongliver/술 잘 마시는 법2.txt'),
    resource.path_for('strongliver/술 잘 마시는 법3.txt'),
    resource.path_for('strongliver/술 잘 마시는 법4.txt'),
    resource.path_for('strongliver/술 잘 마시는 법5.txt'),
    resource.path_for('strongliver/술 잘 마시는 법6.txt'),
    resource.path_for('strongliver/술 잘 마시는 법7.txt'),
]


class Strongliver(InfoProvider):
    def extract_args(self, text):
        return True

    def get_info(self, args):
        return random.choice(TEXTS)

    def info_to_message(self, args, info):
        with open(info) as f:
            return Message(
                text=f.read(),
            )
