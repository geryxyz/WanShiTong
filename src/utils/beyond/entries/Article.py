
# from ...Filter import Filter
from typing import List
from .BaseEntry import BaseEntry

class Article(BaseEntry):
    index: int
    author: str
    title: str
    journal: str
    year: int
    volume: int
    # number: int
    pages: int
    month: int
    note: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)