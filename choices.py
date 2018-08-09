from typing import Tuple, Any


class Choice(str):

    def __new__(cls, value, text):
        obj = str.__new__(cls, value)
        obj.text = text
        return obj


class EnumChoices:

    @classmethod
    def iter(cls):
        for item in dir(cls):
            if isinstance(item, Choice):
                yield item

    @classmethod
    def to_tuple(cls) -> Tuple[Tuple[str, Any]]:
        return tuple((str(item), item.text) for item in cls.iter())
