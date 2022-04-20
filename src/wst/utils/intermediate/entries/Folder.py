from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .BaseEntry import BaseEntry
from typing import List, Optional, Union


class Folder(BaseEntry):
    """
    List of folders
    """
    id: int
    name: str
    parent: Union[None, int]
    userid: int
