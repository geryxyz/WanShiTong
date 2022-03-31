import re
from typing import List


class Datum(object): # singular of data
    @property
    def name(self):
        return 'Aang'


class Filter(object):
    def __init__(self, target: property):
        self.target: property = target

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class Article:
    @property
    def title(self):
        ...


class ContainsTitleFilter(Filter):
    def __init__(self, text: str):
        super().__init__(Article.title)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class TitleFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class ContainsFilter(Filter):
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)


def get_article(*filters: Filter) -> List[Article]:
    ...


for article in articles:
    is_pass = True
    for filter in filters:
        is_pass = filetr.is_pass(article) or is_pass




if __name__ == '__main__':
    get_article(ContainsFilter(Article.title, "kiskutya"))


    datum = Datum()

    print(f'{Datum.name = }')
    print(f'{datum.name = }')
    print(f'{Datum.name.fget(datum) = }')

    name_filter = Filter(Datum.name, r'[Aa]?')
    print(f'{name_filter.is_pass(datum) = }')
