
from pony.orm import * 

class App(db.Entity):
    idApp = PrimaryKey(int, auto=True)
    name = Optional(str)
    description = Optional(str)
    version = Optional(str)
    create_ts = Optional(str)
    app_languages = Set('App_Language')
    notification = Optional('Notification')
