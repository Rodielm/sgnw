
from typing import (Optional, List)
from datetime import date
from pydantic import BaseModel
from .app import *
from .user import *
from .NotifyState import NotifyStateBase
from .group import *
from .rol import *


class NotificationBase(BaseModel):
    summary: str
    summary_args: dict
    body: str
    body_args: dict
    hints: dict
    app: AppBase
    I10n_vers = str
    expire_ts = date

class NotificationInCreate(NotificationBase):
    user: List[UserNotification]
    status: NotifyStateBase
    recipient_user: bool
    recipient_groups: List[GroupNotification]
    recipient_roles: List[RoleNotification]
    pass

class NotificationInResponse(NotificationBase):
    pass


class NotificationInDB(NotificationBase):
    pass


class NotificationInUpdate(NotificationBase):
    pass


class ManyNotificationsInResponse(NotificationBase):
    notifications: List[NotificationBase]
