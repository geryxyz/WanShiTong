from .BaseEntry import BaseEntry
# from ...Filter import Filter
from typing import List


class Booklet(BaseEntry):
    index: int
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

    @classmethod
    def getname(cls):
        return "Booklet"
