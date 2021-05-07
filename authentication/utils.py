from enum import Enum


class Gender(Enum):
    Male = 'male'
    Female = 'female'

    @classmethod
    def choice(cls):
        return [(key.value, key.name) for key in Gender]
