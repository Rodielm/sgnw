

from pony.orm import *
from .base import db


class Argument(db.Entity):
    idArgument = PrimaryKey(int, auto=True)
    name = Optional(str)
    type = Optional(str)  # summary or body
