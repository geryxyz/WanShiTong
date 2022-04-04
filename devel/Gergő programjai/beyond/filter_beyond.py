"""
EXAMPLE USAGE
article1
Filter(Article).Contains(articl1.author, "kismacska")
ArticleProcessor = articles() => tárolja az összes Article példányt

"""

from pydantic import BaseModel
from pydantic.fields import ModelField
import json
from typing import List, Union


class Article(BaseModel):
    title: str
    author: str
    journal: str
    pages: int

    @classmethod
    def get_field_names(cls,alias=False):
        """
        It returns the entries fields
        :param alias:
        :return:
        """
        return list(cls.schema(alias).get("properties").keys())

class Filter:
    target: BaseModel
    field: ModelField
    def __init__(self):
        x=1
        print(x)

    def Contains(self, field, value):
        return field in value

if __name__ == '__main__':
    with open("test_data.json") as file:
        data = json.load(file)
        articles: List[Article] = [Article(**item) for item in data]
    at = articles[0]

    Filter().Contains(Article.__fields__['title'], "kiscica")




