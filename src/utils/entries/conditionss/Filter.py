"""
example usage: Filter("title", "kiskutya")
"""
from pydantic import BaseModel
from pydantic.fields import ModelField


class Filter():
    def __init__(self):
        pass


class Contains(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__()
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        x = getattr(target, self.field.name)
        return self.text in x


class Matches(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__()
        self.text = text
        self.field = field


class NotContains(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__()
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text not in getattr(target, self.field.name)


class NotMatches(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__()
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text != getattr(target, self.field.name)


class Equals(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text == getattr(target, self.field.name)


class NotEquals(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text != getattr(target, self.field.name)


class Equals_or_less(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text <= getattr(target, self.field.name)


class Equals_or_more(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text >= getattr(target, self.field.name)


class Less_than(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text < getattr(target, self.field.name)


class More_than(Filter):
    def __init__(self, field: ModelField, value: int):
        super().__init__()
        self.text = value
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text > getattr(target, self.field.name)
