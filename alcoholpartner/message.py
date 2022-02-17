"""
텔레그램에 보낼 메시지와 보내는 방법을 구현한 코드입니다.

"""
import telegram


class Message(object):
    def __init__(self, text, images=None):
        super().__init__()
        self.text = text
        self.images = images or []

    def send(self, bot: telegram.Bot, chat_id):
        if self.text:
            bot.send_message(chat_id=chat_id, text=self.text)
        for image in self.images:
            with open(image, mode='rb') as f:
                bot.send_photo(chat_id=chat_id, photo=f)
