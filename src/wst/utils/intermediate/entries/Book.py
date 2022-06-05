#https://www.bibtex.com/e/book-entry/
from ..entries.BaseEntry import BaseEntry
from typing import List, Optional
import pydantic


class Book(BaseEntry):
    citekey: Optional[str] = pydantic.Field(title="Citekey", visible_on_gui=False, visible_on_browsing=False, description="")
    author: str = pydantic.Field(title="Author", visible_on_gui=True, description="The person or persons who wrote the article.")
    title: str = pydantic.Field(title="Keyword", visible_on_gui=True, description="The name of the book.")
    publisher: str = pydantic.Field(title="Publisher", visible_on_gui=True, description="The publisher of the book.")
    year: int = pydantic.Field(title="Year", visible_on_gui = True, description="The year the book was published.")
    volume: Optional[str] = pydantic.Field(title="Volume", visible_on_gui=True, description="The volume of the work in the series.")
    number: Optional[int] = pydantic.Field(title="Number", visible_on_gui=True, description="The number of the volume within the series.")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def getname(cls):
        return "Book"

    @classmethod
    def getGuiFields(cls, visible_on_gui, isTitle):
        """

        @param visible_on_gui: return if the field is visible on gui
        @type visible_on_gui: bool
        @param isTitle: if True, returns the Title of the field's the name
        @type isTitle: bool.
        @return:
        @rtype:
        """
        x = cls.__fields__
        coll = []
        for i in x:
            if x[i].field_info.extra["visible_on_gui"] and visible_on_gui is True:
                if isTitle:
                    coll.append(x[i].field_info.title)
                else:
                    coll.append(x[i].name)
            elif visible_on_gui is False:
                if isTitle:
                    coll.append(x[i].field_info.title)
                else:
                    coll.append(x[i].name)
        return coll
