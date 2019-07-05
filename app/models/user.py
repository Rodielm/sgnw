from datetime import datetime

from pony.orm import * 

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
