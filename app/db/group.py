
from pony.orm import *
from .base import db 

class Group(db.Entity):
    idGroup = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    create_ts = Optional(str)
    user_groups = Set('UserGroup')