from ..entries.BaseEntry import BaseEntry
from typing import List



class Book(BaseEntry):
    index: int
    author: str
    title: str
    year: int
    translator: str
    language: str
    volume: str
    publisher: str
    month: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def getname(cls):
        return "Book"

