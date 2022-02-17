import enum


class Level(enum.IntEnum):
    LEVEL1 = 0
    LEVEL2 = 20
    LEVEL3 = 40
    LEVEL4 = 60
    LEVEL5 = 80


def get_level(score):
    last = Level.LEVEL1
    for level in Level:
        if score < level:
            return last
        last = level
    return Level.LEVEL5
