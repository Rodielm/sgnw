
from typing import (Optional, List)
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    

class UserNotification(BaseModel):
    id:int
    username:str

class UserInResponse(UserBase):
    pass

class UserInDB(UserBase):
    password: str

class UserInUpdate(UserBase):
    pass

class ManyUsersInResponse(UserBase):
    users: List[UserBase]
