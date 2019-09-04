
from typing import (List, Optional)
from datetime import date
from pydantic import BaseModel

from .user import *
from .NotifyState import NotifyStateBase
from .group import *
from .rol import *
from .app import *


class NotificationBase(BaseModel):
    summary: str
    summary_args: dict = {}
    body: str
    body_args: dict = {}
    body_type: str = ""
    hints: dict = {}
    app: AppNotification
    I10n_vers: Optional[str] = ""
    expire_ts: date = None


class NotificationInCreate(NotificationBase):
    users: List[UserNotification] = None
    recipient_groups: List[GroupNotification] = None
    recipient_roles: List[RoleNotification] = None
    pass


class UserNotifyStatus(BaseModel):
    idNoti: int
    idStatus: int


class NotificationInResponse(NotificationBase):
    id: int
    pass


class NotificationInDB(NotificationBase):
    pass


class NotificationInUpdate(NotificationBase):
    pass


class ManyNotificationsInResponse(NotificationBase):
    notifications: List[NotificationBase]
