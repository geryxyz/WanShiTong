from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .BaseEntry import BaseEntry
from typing import List, Optional

class Folder(BaseEntry):
    """
    List of folders
    """
    id: int
    Name: str
    title: str
    parent: int
    userid: int