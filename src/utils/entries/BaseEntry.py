from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class BaseEntry(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)