from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from BaseEntry import BaseEntry
from ..Filter import Filter

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


    

class TitleFilter(Filter):
    def __init__(self):
        super().__init__(Article.title)

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()