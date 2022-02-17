"""
정보 제공자의 타입입니다.

"""

from .message import Message


class InfoProvider(object):
    def extract_args(self, text):
        pass

    def get_info(self, args):
        pass

    def info_to_message(self, args, info) -> Message:
        pass
