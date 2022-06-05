from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import pydantic


class BaseEntry(BaseModel):
    # citekey: str = pydantic.Field(title="Keyword", visible_on_gui=False, visible_on_browsing=False, description="")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @classmethod
    def get_field_names(cls,alias=False):
        return list(cls.schema(alias).get("properties").keys())

