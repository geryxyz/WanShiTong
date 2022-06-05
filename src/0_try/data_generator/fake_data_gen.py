from src.wst.utils.intermediate import *
from faker import Faker


x = Article.getTitle("note")
print(x)


def d_g():
    f = Faker()
    for i in range(0, 500):
        author = f.first_name() + " " + f.last_name()
        print(author)
        title = f.bs()
        journal = f.catch_phrase()
        year = int(f.year())
        x = {"author": author, "title": title, "journal": journal, "year": year}
        a = Article(x)
