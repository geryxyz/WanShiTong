"""
example usage: Filter("title", "kiskutya")
"""
from pydantic import BaseModel
from pydantic.fields import ModelField


class Filter():
    def __init__(self, field: ModelField, text: str):
        self.text = text
        self.field = field


class intFilter(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        try:
            value = int(text)
        except ValueError:
            raise ValueError('Please enter an integer')


class strFilter(Filter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        if (len(text) < 1):
            raise ValueError("Empty texts cannot be used!")


class Contains(strFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        x = getattr(target, self.field.name)
        return self.text in x



class Matches(strFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text == getattr(target, self.field.name)


class NotContains(strFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = text
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text not in getattr(target, self.field.name)


class NotMatches(strFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text != getattr(target, self.field.name)


class Equals(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text == getattr(target, self.field.name)


class NotEquals(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text != getattr(target, self.field.name)


class Equals_or_less(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text >= getattr(target, self.field.name)


class Equals_or_more(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text <= getattr(target, self.field.name)


class Less_than(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text > getattr(target, self.field.name)


class More_than(intFilter):
    def __init__(self, field: ModelField, text: str):
        super().__init__(field, text)
        self.text = int(text)
        self.field = field

    def is_pass(self, target: BaseModel) -> bool:
        return self.text < getattr(target, self.field.name)
