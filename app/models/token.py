
from datetime import datetime
from pony.orm import * 


class Token(db.Entity):
    idToken = PrimaryKey(int, auto=True)
    idUser = Optional(str)
    token = Optional(str)
    token_expires = Optional(datetime)