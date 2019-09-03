from datetime import date
from datetime import datetime

from pony.orm import *
from .base import db


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Optional(str)
    username = Required(str)
    password = Required(str)
    config = Optional(Json)
    isActive = Required(bool, default=True)
    isAdmin = Required(bool, default=False)
    create_ts = Optional(date, default=lambda: date.today())
    tokens = Set('Token')
    notify_users = Set('NotifyUser')
    groups = Set('Group')
    roles = Set('Role')


class Role(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    app = Optional('App')
    composite_key(name, app)
    description = Optional(str)
    isActive = Required(bool, default=True)
    create_ts = Optional(date, default=lambda: date.today())
    users = Set(User)
    notify_users = Set('NotifyUser')


class Group(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    app = Optional('App')
    composite_key(name, app)
    description = Optional(str)
    isActive = Required(bool, default=True)
    create_ts = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    users = Set(User)
    notify_users = Set('NotifyUser')


class App(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Optional(str)
    version = Optional(str)
    isActive = Required(bool, default=True)
    create_ts = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    notifications = Set('Notification')
    app_langs = Set('App_lang')
    groups = Set('Group')
    roles = Set('Role')


class Token(db.Entity):
    id = PrimaryKey(int, auto=True)
    token = Required(str)
    token_expires = Optional(datetime)
    user = Required(User)


class Lang(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    isActive = Required(bool, default=True)
    app_langs = Set('App_lang')


class App_lang(db.Entity):
    app = Required(App)
    lang = Required(Lang)
    version = Optional(str)
    filename = Required(str)
    PrimaryKey(app, lang)


class Notification(db.Entity):
    id = PrimaryKey(int, auto=True)
    summary = Optional(str)
    summary_args = Optional(Json)
    body = Optional(str)
    body_args = Optional(Json)
    body_type = Optional(str)
    hints = Optional(Json)
    app = Required(App)
    I10n_vers = Optional(str)
    create_ts = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    expire_ts = Optional(date)
    notify_users = Set('NotifyUser')


class NotifyUser(db.Entity):
    notification = Required('Notification')
    user = Required('User')
    status = Required('NotifyState')
    recipient_user = Required(bool, default=False, sql_default='0')
    recipient_groups = Set('Group')
    recipient_roles = Set('Role')
    composite_key(notification, user)


class NotifyState(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    notify_users = Set(NotifyUser)
