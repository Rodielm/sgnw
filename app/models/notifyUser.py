
from typing import (Optional, List)
from datetime import date
from pydantic import BaseModel
from .notification import NotificationBase
from .user import UserBase
from .rol import RoleBase
from .group import GroupBase
from .NotifyState import NotifyStateBase

class NotifyUserBase(BaseModel):
    notification: NotificationBase
    user: UserBase
    status: NotifyStateBase
    recipient_user: bool
    recipient_group:List[GroupBase]
    recipient_roles:List[RoleBase]


class NotifyUserInResponse(NotifyUserBase):
    pass


class NotifyUserInDB(NotifyUserBase):
    pass


class NotifyUserInUpdate(NotifyUserBase):
    pass


class ManyNotifyUsersInResponse(NotifyUserBase):
    notifications: List[NotifyUserBase]
