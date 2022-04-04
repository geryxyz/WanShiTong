from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from typing import List, Optional

class Folder(BaseModel):
    id: int
    Name: str
    title: str
    parent: int
    content: List[int] = []
    userid: int