from BaseEntry import BaseEntry
from src.utils.Filter import Filter
from typing import List

class Article(BaseEntry):
    author: str
    title: str
    journal: str
    year: int
    volume: int
    number: int
    pages: int
    month: int
    note: str

    @property
    def title(self):
        return self.author

    @property
    def journal(self):
        return self.journal

    @property
    def year(self):
        return self.year

    @property
    def volume(self):
        return self.volume

    @property
    def number(self):
        return self.number

    @property
    def pages(self):
        return self.pages

    @property
    def month(self):
        return self.month

    @property
    def note(self):
        return self.note

#TODO: ddd
    

class TitleFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class AuthorFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class JournalFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class YearFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class VolumeFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class NumberFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class PagesFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()

class MonthFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()
class NoteFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()


class ContainsTitleFilter(Filter):
    def __init__(self, text: str):
        super().__init__(Article.title)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class ContainsYearFilter(Filter):
    def __init__(self, text: str):
        super().__init__(Article.title)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class ContainsJournalFilter(Filter):
    def __init__(self, text: str):
        super().__init__(Article.title)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

class ContainsVolumeFilter(Filter):
    def __init__(self, text: str):
        super().__init__(Article.title)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)

def get_article(*filters: Filter) -> List[Article]:
    pass

