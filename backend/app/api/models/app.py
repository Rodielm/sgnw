
from typing import (Optional, List)
from pydantic import BaseModel
from .master import MasterBase, MasterInResponse


class AppBase(BaseModel):
    name: str
    description: str = None
    version: str = ''


class AppLangBase(BaseModel):
    lang: MasterInResponse
    version: str
    filename: str


class AppCreate(AppBase):
    app_langs: List[AppLangBase] = []


class AppInResponse(AppCreate):
    id: int
    pass


class AppNotification(BaseModel):
    id: int
    name: str = None


class AppInDB(AppBase):
    pass


class AppInUpdate(AppCreate):
    pass


class ManyAppsInResponse(AppBase):
    apps: List[AppBase]
