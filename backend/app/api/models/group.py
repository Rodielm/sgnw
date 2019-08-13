from typing import (Optional, List)
from pydantic import BaseModel

from datetime import datetime
from .app import AppBase


class GroupBase(BaseModel):
    name: str
    description: str
    app: AppBase = None


class GroupNotification(BaseModel):
    name: str


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
