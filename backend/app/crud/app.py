
from typing import List
from pony.orm import *
from app.api.models.app import *
from app.api.models.master import MasterBase
from app.db.base import db


@db_session
def read_apps() -> List[AppInResponse]:
    apps: List[AppInResponse] = []
    rows = select(r for r in db.App)[:]
    for row in rows:
        app = row.to_dict()
        if row.app_langs is not None:
            langs: List[AppLangBase] = []
            for al in row.app_langs:
                applang = AppLangBase(
                    lang=al.lang.to_dict(),
                    filename=al.filename,
                    version=al.version)
                langs.append(applang)
            app['app_langs'] = langs
        apps.append(app)
    return apps


@db_session
def read_app_for_name(name: str) -> AppInResponse:
    row = db.App.get(name=name)
    if row:
        return row.to_dict()


@db_session
def create_app(row: AppCreate):

    app = db.App(
        name=row.name,
        description=row.description,
        version=row.version,
    )

    if row.app_langs:
        for lang in row.app_langs:
            l = db.Lang.get(id=lang.lang.id)
            db.App_lang(
                app=app,
                lang=l,
                version=lang.version,
                filename=lang.filename)

    return row


@db_session
def update_app(id: int, app: AppInUpdate):
    dbapp = db.App.get(id=id)
    if not dbapp:
        return dbapp
    else:
        dbapp.name = app.name
        commit()
    return dbapp


@db_session
def delete_app(id: int):
    db.app[id].delete()
