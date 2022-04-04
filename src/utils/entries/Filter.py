from ..Filter import Filter

class ContainsFilter(Filter):
    """
    If the Article's field contains a value

    """
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class EQFilter(Filter):
    """
    Eq = Equals
    If the Article's field equals a value. We use this for numbers only.
    #TODO: But what if we use for a string?
    """
    def __init__(self, target, number: int):
        super().__init__(target)
        self._number = number

    def is_pass(self, entity) -> bool:
        return self._number == self.target.fget(entity)

class EOLFilter(Filter):
    """
    EOL = Equals or Less
    If the Article's field equals or less than a value. We use this for numbers only.
    """
    def __init__(self, target, number: int):
        super().__init__(target)
        self._number = number

    def is_pass(self, entity) -> bool:
        return self._number <= self.target.fget(entity)

class EOMFilter(Filter):
    """
    EOM = Equals or More
    If the Article's field equals or more than a value. We use this for numbers only.
    """
    def __init__(self, target, number: int):
        super().__init__(target)
        self._number = number

    def is_pass(self, entity) -> bool:
        return self._number >= self.target.fget(entity)

class MoreThanFilter(Filter):
    """
    If the Article's field more than a value. We use this for numbers only.
    """
    def __init__(self, target, number: int):
        super().__init__(target)
        self._number = number

    def is_pass(self, entity) -> bool:
        return self._number > self.target.fget(entity)

class LessThanFilter(Filter):
    """
    If the Article's field more than a value. We use this for numbers only.
    """
    def __init__(self, target, number: int):
        super().__init__(target)
        self._number = number

    def is_pass(self, entity) -> bool:
        return self._number < self.target.fget(entity)

#Its not necessary to have these classes, it can be done by a Not Logic statement
# class NotEqualsFilter(Filter):
#     """
#     If the Article's field not equals to a value. We use this for numbers only.
#     """
#     def __init__(self, target, number: int):
#         super().__init__(target)
#         self._number = number
#
#     def is_pass(self, entity) -> bool:
#         return self._number != self.target.fget(entity)
#
# class NotContainsFilter(Filter):
#     """
#     If the Article's field not contains a value. We use this for texts only.
#     """
#     def __init__(self, target, text: str):
#         super().__init__(target)
#         self._text = text
#
#     def is_pass(self, entity) -> bool:
#         return self._text not in self.target.fget(entity)

class MatchWithFilter(Filter):
    """
    If the Article's field match with a value. We use this for texts only.
    """
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text == self.target.fget(entity)

