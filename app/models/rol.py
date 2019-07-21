
from typing import (Optional, List)
from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    
# Response means out like UserOut...

class RoleInResponse(RoleBase):
    id:int
    pass

class RoleInDB(RoleBase):
    pass

class RoleInUpdate(RoleBase):
    pass

class ManyRolesInResponse(RoleBase):
    roles: List[RoleBase]
