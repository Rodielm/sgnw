from datetime import datetime
from pony.orm import *


db = Database()


class User(db.Entity):
    idUser = PrimaryKey(int, auto=True)
    first_name = Optional(str)
    last_name = Optional(str)
    email = Optional(str)
    username = Optional(str)
    password = Optional(str)
    create_ts = Optional(str)
    user_groups = Set('UserGroup')
    user_roles = Set('UserRole')
    user_recipients = Set('UserRecipient')


class App(db.Entity):
    idApp = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    version = Optional(str)
    create_ts = Optional(str)
    app_languages = Set('App_Language')
    notification = Optional('Notification')


class Token(db.Entity):
    idToken = PrimaryKey(int, auto=True)
    idUser = Optional(str)
    token = Optional(str)
    token_expires = Optional(datetime)


class Argument(db.Entity):
    idArgument = PrimaryKey(int, auto=True)
    name = Optional(str)
    type = Optional(str)  # summary or body


class Role(db.Entity):
    idRol = PrimaryKey(int, auto=True)
    name = Optional(str)
    user_roles = Set('UserRole')


class Group(db.Entity):
    idGroup = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    create_ts = Optional(str)
    user_groups = Set('UserGroup')


class App_Language(db.Entity):
    app = Required(App)
    language = Required('Language')


class Language(db.Entity):
    idLanguage = PrimaryKey(int, auto=True)
    name = Optional(str)
    app_languages = Set(App_Language)


class Notification(db.Entity):
    idNotification = PrimaryKey(int, auto=True)
    summary = Optional(str)
    body = Optional(str)
    I10n_vers = Optional(str)
    create_ts = Optional(str)
    expire_ts = Optional(str)
    app = Required(App)
    recipients = Set('Recipient')


class Recipient(db.Entity):
    idRecipient = PrimaryKey(int, auto=True)
    user_recipients = Set('UserRecipient')
    user_roles = Set('UserRole')
    user_groups = Set('UserGroup')
    notification = Required(Notification)


class UserGroup(db.Entity):
    group = Required(Group)
    user = Required(User)
    recipient = Optional(Recipient)


class UserRole(db.Entity):
    user = Required(User)
    role = Required(Role)
    recipient = Optional(Recipient)


class UserRecipient(db.Entity):
    recipient = Required(Recipient)
    user = Required(User)



db.generate_mapping()