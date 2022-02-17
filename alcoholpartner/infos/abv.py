"""
알콜 도수를 알려주는 정보제공자입니다.

"""

import itertools

from alcoholpartner.info import InfoProvider
from alcoholpartner.message import Message

ABVS = {
    '소주': 19,
    '막걸리': 6,
    '맥주': 4.5,
    '레드와인': 13,
    '화이트와인': 10,
    '와인': 13,
    '위스키': 45,
}


class ABVInfo(InfoProvider):
    def extract_args(self, text):
        matched_names = []
        for name in ABVS:
            if name in text:
                matched_names.append(name)
                break
        if not matched_names:
            return None

        # 유사한 이름에 매칭되었을 때 우선순위를 정합니다.
        # 예를들어 "레드와인 도수 알려줘"는 "와인"과 "레드와인"에 모두
        # 매칭되지만, 단어 "와인"은 "레드와인"에 포함되기에, 우선순위를
        # 낮춥니다.
        removed = []
        for left, right in itertools.combinations(matched_names, 2):
            if left in removed or right in removed:
                continue
            if left == right:
                continue
            if left in right:
                removed.append(left)
            elif right in left:
                removed.append(right)
        matched_names = [x for x in matched_names if x not in removed]

        return {
            'name': matched_names[0]
        }

    def get_info(self, args):
        name = args['name']
        return {
            'ABV': ABVS[name],
        }

    def info_to_message(self, args, info):
        name = args['name']
        abv = info['ABV']

        return Message(
            f"{name}의 평균 도수는 {abv}% 입니다.\n출처: https://www.fatsecret.kr"
        )
