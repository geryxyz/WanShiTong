from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Folder(BaseModel):
    id: int
    Name: str
    Title: str
    Parent: int
    content: tuple
