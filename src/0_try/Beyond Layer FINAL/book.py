from BaseEntry import BaseEntry
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


