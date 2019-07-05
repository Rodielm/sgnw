from pony.orm import * 
from .app import App

class App_Language(db.Entity):
    app = Required(App)
    language = Required('Language')
