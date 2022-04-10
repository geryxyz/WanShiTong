from .BaseEntry import BaseEntry
# from ...Filter import Filter
from typing import List


class Booklet(BaseEntry):
    author: str
    title: str
    year: int
    pages: int
    howpublished: str #??
    language: str
    type: str
    url: str
    note: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)