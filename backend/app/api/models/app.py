
from typing import (Optional, List)
from pydantic import BaseModel
from .master import MasterBase

class AppBase(BaseModel):
    name: str
    description: str = None
    version: str = ''

class AppNotification(BaseModel):
    id:int
    name:str = None
    
class AppInResponse(AppBase):
    id:int
    pass

class AppInDB(AppBase):
    pass

class AppInUpdate(AppBase):
    pass

class ManyAppsInResponse(AppBase):
    apps: List[AppBase]
