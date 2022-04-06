from ..BaseEntry import BaseEntry
# from ...Filter import Filter
from typing import List


class Thesis(BaseEntry):
    author: str
    title: str
    type: str
    institution: str
    year: int
    language: str
    note: str
    month: int
    isbn: str
    pages: int
    url: str