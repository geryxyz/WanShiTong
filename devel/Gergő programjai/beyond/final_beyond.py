import re
from typing import List,Union
from pydantic import BaseModel
from pydantic.fields import ModelField
from var_dump import var_dump
import json

class Datum(object): # singular of data
    """
    It's just a pydantic object, it can be Article too
    """
    @property
    def name(self):
        return 'Aang'


class Article(BaseModel):
    title: str
    author: str
    journal: str
    pages: int

    @classmethod
    def get_field_names(cls,alias=False):
        """
        It returns the entries fields
        :param alias:
        :return:
        """
        return list(cls.schema(alias).get("properties").keys())




class Filter(object):
    """
    The main Filter object
    """
    def __init__(self, target: ModelField ):
        self.target: ModelField = target

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class ContainsFilter(Filter):
    """
    A child of the main Filter object
    """
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text
        self.is_pass()

    def is_pass(self, entity: BaseModel) -> bool:
        # return self._text in self.target.fget(entity)
        alma: ModelField = entity.__fields__[self.target.name]
        return self._text in entity.__fields__[self.target.name]

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
        #todo *conditons
        super().__init__(condition1, condition2)
        self._cond1 = condition1
        self._cond2 = condition2

    def is_pass(self, entity) -> bool:
        return self._cond1.is_pass(entity) and self._cond2.is_pass(entity)

class TrueLogic(Logic):
    def __init__(self, condition):
        super().__init__(condition)
        self._cond1 = condition
        # self._cond2 = condition

    def is_pass(self, entity) -> bool:
        return self._cond1



def get_article(*filters: Union[Logic,Filter]) -> List[Article]:
    filters[0].is_pass(Article(title="kutya", author="cica", journal="kakas"))
    resume = []
    return resume


c
    # get_article(TrueLogic(ContainsFilter(Article.title, "kiskutya")))
    # get_article(AndLogic(ContainsFilter(Article.__fields__['title'], "kismacska"), ContainsFilter(Article.__fields__['title'], "kiskutya")))
    # get_article(BiggerFilter(article.page, 9))
    with open("test_data.json") as file:
        data = json.load(file)
        articles: List[Article] = [Article(**item) for item in data]
    ar_1 = articles[0]
    # print(ContainsFilter(Article, Article.author)
    # teszt = list(Article.__fields__.keys())
    # teszt2 = Article.get_field_names()
    type(Article.title)


    for i in teszt:
        print(i)

        # print(i) #->title, author, journal
    # var_dump(teszt)


    """
    #0 object(mappingproxy) ({'__module__': '__main__', '__annotations__': {'title': <class 'str'>, 'author': <class 'str'>, 'journal': <class 'str'>}, 'title': <property object at 0x00000241CC4B53B8>, '__dict__': <attribute '__dict__' of 'Article' objects>, '__weakref__': <attribute '__weakref__' of 'Article' objects>, '__doc__': None})
    """