from datetime import date
from datetime import datetime

from pony.orm import *
from .base import db 

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Optional(str)
    last_name = Optional(str)
    email = Optional(str)
    username = Optional(str)
    password = Optional(str)
    create_ts = Optional(date)
    groups = Set('Group')
    roles = Set('Role')
    recipients = Set('Recipient')
    tokens = Set('Token')


class App(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    version = Optional(str)
    create_ts = Required(datetime,sql_default='CURRENT_TIMESTAMP')
    languages = Set('Language')
    notifications = Set('Notification')


class Token(db.Entity):
    id = PrimaryKey(int, auto=True)
    token = Optional(str)
    token_expires = Optional(datetime)
    user = Required(User)


class Argument(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    type = Optional(str)  # summary or body


class Role(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    users = Set(User)
    recipients = Set('Recipient')


class Group(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    create_ts = Required(datetime,sql_default='CURRENT_TIMESTAMP')
    users = Set(User)
    recipients = Set('Recipient')


class Language(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    apps = Set(App)


class Notification(db.Entity):
    id = PrimaryKey(int, auto=True)
    summary = Optional(str)
    body = Optional(str)
    body_type = Required('BodyType')
    hints = Optional(str)
    app = Required(App)
    recipient = Optional('Recipient')
    I10n_vers = Optional(str)
    create_ts = Optional(date)
    expire_ts = Optional(date)


class Recipient(db.Entity):
    id = PrimaryKey(int, auto=True)
    users = Set(User)
    notifications = Set(Notification)
    roles = Set(Role)
    groups = Set(Group)


class BodyType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    type = Optional(str)
    create_ts = Optional(date)
    notifications = Set(Notification)


