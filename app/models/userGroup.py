
from pony.orm import * 
from .recipient import Recipient
from .user import User
from .group import Group


class UserGroup(db.Entity):
    group = Required(Group)
    user = Required(User)
    recipient = Optional(Recipient)