from ..BaseEntry import BaseEntry
# from ...Filter import Filter
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


