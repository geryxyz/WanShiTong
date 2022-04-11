from final_beyond import *
import json

class Article(BaseModel):
    title: str
    author: str
    journal: str
    pages: int


def get_article(*filters: Union[Logic,Filter]) -> List[Article]:
    filters[0].is_pass(Article(title="kutya", author="cica", journal="kakas"))
    resume = []
    return resume

if __name__ == '__main__':
    # get_article(TrueLogic(ContainsFilter(Article.title, "kiskutya")))
    # get_article(AndLogic(ContainsFilter(Article.__fields__['title'], "kismacska"), ContainsFilter(Article.__fields__['title'], "kiskutya")))

    with open("./test_data.json") as file:
        data = json.load(file)
        articles: List[Article] = [Article(**item) for item in data]


    # get_article(BiggerFilter(article.page, 9))

    teszt = list(Article.__fields__.keys())
    for i in teszt:
        print(i)

