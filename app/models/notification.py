
from typing import (Optional, List)
from datetime import date
from pydantic import BaseModel
from .app import AppBase


class NotificationBase(BaseModel):
    summary: str
    summary_args: dict
    body: str
    body_args: dict
    hints: dict
    app: AppBase
    I10n_vers = str
    expire_ts = date


class NotificationInResponse(NotificationBase):
    pass


class NotificationInDB(NotificationBase):
    pass


class NotificationInUpdate(NotificationBase):
    pass


class ManyNotificationsInResponse(NotificationBase):
    notifications: List[NotificationBase]
