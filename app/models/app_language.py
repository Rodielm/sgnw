from pony.orm import *
from .base import db
from .app import App


class App_Language(db.Entity):
    app = Required(App)
    language = Required('Language')
