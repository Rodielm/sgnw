
from typing import (Optional, List)
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str = ""
    username: str = ""
    


class UserSecurity(UserBase):
    id: int
    isActive: bool
    isAdmin: bool
    pass


class UserNotification(UserBase):
    pass


class UserInResponse(UserBase):
    id: int
    isAdmin: bool
    isActive: bool
    pass


class UserInDB(UserBase):
    password: str


class UserInUpdate(UserBase):
    pass


class ManyUsersInResponse(UserBase):
    users: List[UserBase]
