
from pony.orm import * 
from .app_language import App_Language

class Language(db.Entity):
    idLanguage = PrimaryKey(int, auto=True)
    name = Optional(str)
    app_languages = Set(App_Language)