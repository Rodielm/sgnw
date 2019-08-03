
from typing import (Optional, List)
from pydantic import BaseModel

from datetime import datetime


class GroupBase(BaseModel):
    name: str
    description: str

class GroupNotification(BaseModel):
    id:int
    name:str

class GroupInResponse(GroupBase):
    id: int
    create_ts: datetime
    pass


class GroupInDB(GroupBase):
    pass


class GroupInUpdate(GroupBase):
    pass


class ManyGroupsInResponse(GroupBase):
    Groups: List[GroupBase]
