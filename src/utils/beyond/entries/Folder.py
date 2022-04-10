from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .BaseEntry import BaseEntry
from typing import List, Optional

class Folder(BaseEntry):
    id: int
    Name: str
    title: str
    parent: int
    content: List[int] = []
    userid: int