from BaseEntryyyyy import BaseEntry
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

