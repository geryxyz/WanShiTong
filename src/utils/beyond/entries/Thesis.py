from .BaseEntry import BaseEntry
from typing import List


class Thesis(BaseEntry):
    index: int
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def getname(cls):
        return "Thesis"
