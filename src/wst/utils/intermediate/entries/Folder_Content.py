from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from .BaseEntry import BaseEntry
from typing import List, Optional

class Folder_Content(BaseEntry):
    """
    Content of one Folder
    """
    id: int
    folder: int
    entry_type: str
    citekey: str
