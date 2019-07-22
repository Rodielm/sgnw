
from typing import (Optional, List)
from pydantic import BaseModel
from .master import MasterBase

class AppBase(BaseModel):
    name: str
    description: str
    version: str
    
class AppInResponse(AppBase):
    pass

class AppInDB(AppBase):
    languages:List[MasterBase]
    pass

class AppInUpdate(AppBase):
    pass

class ManyAppsInResponse(AppBase):
    apps: List[AppBase]
