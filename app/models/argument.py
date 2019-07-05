

from pony.orm import * 

class Argument(db.Entity):
    idArgument = PrimaryKey(int, auto=True)
    name = Optional(str)
    type = Optional(str)  # summary or body
