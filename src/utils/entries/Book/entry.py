from ..BaseEntry import BaseEntry
from typing import List


class Book(BaseEntry):
    author: str
    title: str
    year: int
    translator: str
    language: str
    volume: str
    publisher: str
    month: int

    @property
    def title(self):
        return self.title

    @property
    def author(self):
        return self.author

    @property
    def year(self):
        return self.year

    @property
    def translator(self):
        return self.translator

    @property
    def language(self):
        return self.language

    @property
    def volume(self):
        return self.volume

    @property
    def publisher(self):
        return self.publisher

    @property
    def month(self):
        return self.month
