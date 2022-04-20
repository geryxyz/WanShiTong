from .BaseEntry import BaseEntry
# from ...Filter import Filter
from typing import List
from pydantic.fields import ModelField
from typing import Optional
import pydantic

#    author: str = pydantic.Field(title="Author", visible_on_gui=True, description="The person or persons who wrote the article.")
class Booklet(BaseEntry):
    citekey: Optional[str] = pydantic.Field(title="Citekey", visible_on_gui=False, visible_on_browsing=False, description="")
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

    @staticmethod
    def getname():
        return "Booklet"

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