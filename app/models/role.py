
from datetime import datetime
from pony.orm import * 


class Role(db.Entity):
    idRol = PrimaryKey(int, auto=True)
    name = Optional(str)
    user_roles = Set('UserRole')
