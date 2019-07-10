
from datetime import datetime
from pony.orm import *
from .base import db 
from .app import App


class Notification(db.Entity):
    idNotification = PrimaryKey(int, auto=True)
    summary = Optional(str)
    body = Optional(str)
    I10n_vers = Optional(str)
    create_ts = Optional(str)
    expire_ts = Optional(str)
    app = Required(App)
    recipients = Set('Recipient')