from BaseEntry import BaseEntry
# from ...Filter import Filter
from typing import List


class Article(BaseEntry):
    author: str
    title: str
    journal: str
    pages: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print("heló")
