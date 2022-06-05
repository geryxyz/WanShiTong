from .BaseEntry import BaseEntry
from typing import List


class Thesis(BaseEntry):
    index: int
    author: str
    title: str
    type: str
    institution: str
    year: int
    language: str
    note: str
    month: int
    isbn: str
    pages: int
    url: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def getname(cls):
        return "Thesis"

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