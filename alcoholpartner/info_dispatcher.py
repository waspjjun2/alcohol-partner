"""
어떤 종류의 정보 제공자에게서 정보를 받을지 결정해주는 구현입니다.

"""
import telegram
from konlpy.tag import Okt

from .infos.abv import ABVInfo
from .infos.hangover import Hangover
from .infos.remedy import Remedy
from .infos.strongliver import Strongliver
from .state import State

tag = Okt()


INFO_MANAGERS = [
    ABVInfo(),
]


def dispatch_info(state: State, update: telegram.Update):
    text = update.message.text
    poses = tag.pos(text, stem=True)

    print(poses)

    nouns = [p for p, c in poses if c == 'Noun']
    units = [p for p, c in poses]

    if '도수' in nouns or \
            (('몇 도' in text or '몇도' in text) and
             ('?', 'Punctuation') in poses):
        return ABVInfo()
    elif ({'숙취', '해소'}.issubset(set(units))) or \
            ('숙취' in units and {'심하다', '심해'} & set(units)):
        return Hangover()
    elif ({'해장', '법'}.issubset(set(units))) or \
            ('속' in units and {'안좋다', '쓰리다', '쓰다'} & set(units)):
        return Remedy()
    if ({'술', '잘', '마시다'}.issubset(set(units)) or
            {'술', '잘', '먹다'}.issubset(set(units)) or
            {'술', '잘', '말다'}.issubset(set(units)) or
            {'술', '많이', '마시다'}.issubset(set(units)) or
            {'술', '많이', '먹다'}.issubset(set(units)) or
            {'술', '먹다', '때', '팁'}.issubset(set(units)) or
            {'술', '말다', '때', '팁'}.issubset(set(units))):
        return Strongliver()
    return None
