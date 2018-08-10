from typing import Tuple, Any


class CachedClassProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if not hasattr(owner, '_tuple'):
            owner._tuple = self.func(owner)
        return owner._tuple


cached_class_property = CachedClassProperty


class Choice(str):

    def __new__(cls, value, text):
        obj = super().__new__(cls, value)
        obj.text = text
        return obj


class EnumChoices:

    @classmethod
    def iter(cls):
        for key, item in cls.__dict__.items():
            if isinstance(item, Choice):
                yield item

    @cached_class_property
    def to_tuple(cls) -> Tuple[Tuple[str, Any]]:
        return tuple((str(item), item.text) for item in cls.iter())
