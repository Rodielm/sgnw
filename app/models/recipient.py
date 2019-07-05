
from datetime import datetime
from pony.orm import * 
from .base import db
from .notification import Notification



class Recipient(db.Entity):
    idRecipient = PrimaryKey(int, auto=True)
    user_recipients = Set('UserRecipient')
    user_roles = Set('UserRole')
    user_groups = Set('UserGroup')
    notification = Required(Notification)