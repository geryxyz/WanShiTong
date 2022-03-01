from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Article(BaseModel):
    Author: str
    Title: str
    Journal : str
    Year : int
    Volume : int
    number : int
    pages : int
    month : int
    note : str
    alias = 'anonymous'
    timestamp: Optional[datetime] = None
    friends: List[int] = []