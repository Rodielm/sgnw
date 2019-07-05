from pony.orm import * 
from .recipient import Recipient
from .user import User

class UserRecipient(db.Entity):
    recipient = Required(Recipient)
    user = Required(User)