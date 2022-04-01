import re
from typing import List
import pydantic

class Datum(object): # singular of data
    """
    It's just a pydantic object, it can be Article too
    """
    @property
    def name(self):
        return 'Aang'


class Article:
    title: str
    @property
    def title(self):
        pass

class Filter(object):
    """
    The main Filter object
    """
    def __init__(self, target: property):
        self.target: property = target

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class ContainsFilter(Filter):
    """
    A child of the main Filter object
    """
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class Logic(object):
    """
    The main Logical object
    """

    def __init__(self, target1: Filter, target2: Filter=None):
        """
        :param target1: It stands for the first parameter. It can be single Logic procedure
        :param target2: Not necessarily must be given. It stands for logical procedures which has two parameters
        """
        self.target1: Filter = target1
        self.target2: Filter = target2

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class AndLogic(Logic):
    def __init__(self, condition1, condition2):
        super().__init__(condition1, condition2)
        self._cond1 = condition1
        self._cond2 = condition2

    def is_pass(self, entity) -> bool:
        return self._cond1 and self._cond2

class TrueLogic(Logic):
    def __init__(self, condition):
        super().__init__(condition)
        self._cond1 = condition
        # self._cond2 = condition

    def is_pass(self, entity) -> bool:
        return self._cond1



def get_article(*filters: Logic) -> List[Article]:
    pass


if __name__ == '__main__':
    get_article(TrueLogic(ContainsFilter(Article.title, "kiskutya")))
    get_article(AndLogic(ContainsFilter(Article.title, "kismacska"), ContainsFilter(Article.title, "kiskutya")))
    # get_article(BiggerFilter(article.page, 9))