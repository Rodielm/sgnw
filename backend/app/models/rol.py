
from typing import (Optional, List)
from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    

class RoleNotification(BaseModel):
    name: str
    
class RoleInResponse(RoleBase):
    id:int
    pass

class RoleInDB(RoleBase):
    pass

class RoleInUpdate(RoleBase):
    pass

class ManyRolesInResponse(RoleBase):
    roles: List[RoleBase]
