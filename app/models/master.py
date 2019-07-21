
from typing import (Optional, List)
from pydantic import BaseModel


class MasterBase(BaseModel):
    name: str

class MasterInResponse(MasterBase):
    id:int
    pass

class MasterInDB(MasterBase):
    pass

class MasterInUpdate(MasterBase):
    pass

class ManyMastersInResponse(MasterBase):
    Masters: List[MasterBase]
