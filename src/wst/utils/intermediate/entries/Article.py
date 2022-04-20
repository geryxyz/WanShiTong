# from ...Filter import Filter
from typing import List
from .BaseEntry import BaseEntry
import pydantic
from pydantic.fields import ModelField
from typing import Optional


class Article(BaseEntry):
    citekey: Optional[str] = pydantic.Field(title="Citekey", visible_on_gui=False, visible_on_browsing=False, description="")
    author: str = pydantic.Field(title="Author", visible_on_gui=True,
                                 description="The person or persons who wrote the article.")
    title: str = pydantic.Field(title="Keyword", visible_on_gui=True, description="The name of the article.")
    journal: str = pydantic.Field(title="Journal", visible_on_gui=True,
                                  description="The name of the work the article was found in.")
    year: int = pydantic.Field(title="Year", visible_on_gui=True, description="The year the article was published.")
    volume: Optional[int] = pydantic.Field(title="Volume", visible_on_gui=True,
                                           description="The volume of the work in the series.")
    number: Optional[int] = pydantic.Field(title="Number", visible_on_gui=True,
                                           description="The number of the volume within the series.")
    pages: Optional[int] = pydantic.Field(title="Pages", visible_on_gui=True,
                                          description="The page number or page range the article is found on.")
    month: Optional[int] = pydantic.Field(title="Month", visible_on_gui=True,
                                          description="The month the article was published.")
    note: Optional[str] = pydantic.Field(title="Note", visible_on_gui=False,
                                         description="Any miscellaneous information that does not qualify for another field.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def getName():
        return "Article"

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

    @classmethod
    def getGuiFieldsWithTitle(cls):
        x = cls.__fields__
        coll = []
        for i in x:
            if x[i].field_info.extra["visible_on_gui"]:
                coll.append(x[i])
        return coll

    @classmethod
    def getTitle(cls, fieldname):
        return cls.__fields__[fieldname].field_info.title

    @classmethod
    def getTitleifGui(cls, fieldname):
        if cls.__fields__[fieldname].field_info.extra["visible_on_gui"]:
            return cls.__fields__[fieldname].field_info.title
        return None

    @classmethod
    def getbrowsingfields(cls):
        raise NotImplementedError()
