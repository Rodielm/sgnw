
from typing import (Optional, List)
from pydantic import BaseModel
from .master import MasterInDB

class AppBase(BaseModel):
    name: str
    description: str
    version: str
    

class AppInResponse(AppBase):
    pass

class AppInDB(AppBase):
    pass

class AppInUpdate(AppBase):
    pass

class ManyAppsInResponse(AppBase):
    apps: List[AppBase]
