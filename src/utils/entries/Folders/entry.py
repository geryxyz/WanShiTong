from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Folder(BaseModel):
    id: int
    Name: str
    title: str
    parent: int
    content: tuple
    userid: int

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def title(self):
        return self.title

    @property
    def parent(self):
        return self.parent

    @property
    def content(self):
        return self.content

    @property
    def userid(self):
        return self.userid