from . import image
from .message import Message


SESSION_STARTED = Message(text="술자리가 시작되었네요!\n즐거운 술자리 가지시고, 과음하지 않도록 주의하세요!")
SESSION_STOPPED = Message(text="즐거운 술자리 되셨나요?\n집까지 안전하게 돌아가세요!")
SESSION_ALREADY_STARTED = Message(text="이미 시작했다고 말씀하셨어요!")
SESSION_ALREADY_STOPPED = Message(text="")

INFO_CANT_UNDERSTAND_MESSAGES = [
    Message(text="무슨 말인지 잘 모르겠어요."),
    Message(text="아직 모르는게 너무 많아서 대답할 수 없어요."),
    Message(text="죄송해요, 다시 물어봐 주시겠어요?"),
]

QUIZ_RIGHT_ANSWER_MESSAGES = [
    Message(text="맞았어요!"),
    Message(text="정답이에요!"),
    Message(text="훌륭해요!"),
]
QUIZ_WRONG_ANSWER_MESSAGES = [
    Message(text="틀렸어요!"),
    Message(text="오답이에요!"),
    Message(text="아쉽네요ㅠㅠ"),
]
QUIZ_NO_RESPONSE_MESSAGES = [
    Message(text="답장을 안해서 오답처리 했어요."),
    Message(text="답장이 없어서 틀렸다고 했어요."),
]

LEVEL1_MESSAGES = [
    Message(
        text="[취한정도: 안취함]\n재밌게 노세요~ :D",
        images=[
            image.path_for('levels/level1/1.jpg')
        ]),
    Message(
        text="[취한정도: 안취함]\n아직 안취했네요!",
        images=[
            image.path_for('levels/level1/2.jpg')
        ]),
    Message(
        text="[취한정도: 안취함]\n이제 시작인가요?",
        images=[
            image.path_for('levels/level1/3.jpg')
        ]),
    Message(
        text="[취한정도: 안취함]\n멀쩡하시네요!",
        images=[
            image.path_for('levels/level1/4.jpg')
        ]),
]
LEVEL2_MESSAGES = [
    Message(
        text="[취한정도: 기분 좋게 취함]\n딱 즐겁네요!",
        images=[
            image.path_for('levels/level2/1.jpg')
        ]),
    Message(
        text="[취한정도: 기분 좋게 취함]\n아직 거뜬하네요!",
        images=[
            image.path_for('levels/level2/2.jpg')
        ]),
    Message(
        text="[취한정도: 기분 좋게 취함]\n기분 조오타~~ 아직은 괜찮아요!",
        images=[
            image.path_for('levels/level2/3.jpg')
        ]),
    Message(
        text="[취한정도: 기분 좋게 취함]\n적당히 기분 좋은 정도네요~",
        images=[
            image.path_for('levels/level2/4.jpg')
        ]),
]
LEVEL3_MESSAGES = [
    Message(
        text="[취한정도: 알딸딸하게 취함]\n더 취하지 않도록 주의하세요!",
        images=[
            image.path_for('levels/level3/1.jpg')
        ]),
    Message(
        text="[취한정도: 알딸딸하게 취함]\n슬슬 조절하세요!",
        images=[
            image.path_for('levels/level3/2.jpg')
        ]),
    Message(
        text="[취한정도: 알딸딸하게 취함]\n알딸딸하시군요~",
        images=[
            image.path_for('levels/level3/3.jpg')
        ]),
    Message(
        text="[취한정도: 알딸딸하게 취함]\n조심 또 조심! 여기서 더 가면 무슨 일이 생길지 몰라요!",
        images=[
            image.path_for('levels/level3/4.jpg')
        ]),
]
LEVEL4_MESSAGES = [
    Message(
        text="[취한정도: 많이 취함]\n많이 취하셨네요 ㅠㅠ",
        images=[
            image.path_for('levels/level4/1.jpg')
        ]),
    Message(
        text="[취한정도: 많이 취함]\n집 가셔야 할 것 같아요~",
        images=[
            image.path_for('levels/level4/2.jpg')
        ]),
    Message(
        text="[취한정도: 많이 취함]\n더 있다가 민폐라도 끼치면….",
        images=[
            image.path_for('levels/level4/2.jpg')
        ]),
    Message(
        text="[취한정도: 많이 취함]\n더 드시면 위험해요!",
        images=[
            image.path_for('levels/level4/1.jpg')
        ]),
]
LEVEL5_MESSAGES = [
    Message(
        text="[취한정도: 인사불성]\n구 애인의 번호는 지우셨나요..?",
        images=[
            image.path_for('levels/level5/1.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n미쳤습니까?",
        images=[
            image.path_for('levels/level5/2.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n당장 귀가하세요.",
        images=[
            image.path_for('levels/level5/3.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n그만 드세요. ",
        images=[
            image.path_for('levels/level5/4.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n연락할 때 주의하세요!",
        images=[
            image.path_for('levels/level5/4.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n멈추세요. ",
        images=[
            image.path_for('levels/level5/3.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n절대 집 가,,",
        images=[
            image.path_for('levels/level5/3.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n이제 그만! 넌 이미 죽었다",
        images=[
            image.path_for('levels/level5/4.jpg')
        ]),
    Message(
        text="[취한정도: 인사불성]\n그만 마셔! ",
        images=[
            image.path_for('levels/level5/3.jpg')
        ]),
]

QUIZ_TYPO_TEXT = "다음 문장을 똑같이 따라치세요."
