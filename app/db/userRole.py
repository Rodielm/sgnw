from datetime import datetime
from pony.orm import * 
from .base import db
from .user import User
from .role import Role
from .recipient import Recipient


class UserRole(db.Entity):
    user = Required(User)
    role = Required(Role)
    recipient = Optional(Recipient)