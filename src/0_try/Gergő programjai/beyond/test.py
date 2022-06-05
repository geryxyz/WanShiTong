from final_beyond import *
import json

import pydantic


class Person(BaseModel):
    name: str
    age: int
    address: str
    mother: str

p = Person(name="Steve", age="Lorem Ipsum", address="Szeged", mother="Julia")

p = Person(name="Steve", age=25, address="Szeged", mother="Julia")

def get_article(*filters: Union[Logic, Filter]) -> List[Article]:
    filters[0].is_pass(Article(title="kutya", author="cica", journal="kakas"))
    resume = []
    return resume


# if __name__ == '__main__':
#

    # get_article(TrueLogic(ContainsFilter(Article.title, "kiskutya")))
    # get_article(AndLogic(ContainsFilter(Article.__fields__['title'], "kismacska"), ContainsFilter(Article.__fields__['title'], "kiskutya")))
    #
    # with open("test_data.json") as file:
    #     data = json.load(file)
    #     articles: List[Article] = [Article(**item) for item in data]
    #
    # # get_article(BiggerFilter(article.page, 9))
    #
    # teszt = list(Article.__fields__.keys())
    # for i in teszt:
    #     print(i)
