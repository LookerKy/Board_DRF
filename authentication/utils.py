from enum import IntEnum


class Gender(IntEnum):
    Male = 1
    Female = 2

    @classmethod
    def choice(cls):
        return [(key.value, key.name) for key in cls]
