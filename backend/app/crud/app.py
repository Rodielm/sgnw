
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
        apps.append(row.to_dict())
    return apps


@db_session
def read_app_for_name(name: str) -> AppInResponse:
    row = db.App.get(name=name)
    if row:
        return row.to_dict()


@db_session
def create_app(row: AppBase):
    # langs: List[MasterBase] = []
    # if row.languages is not None:
    #     for item in row.languages:
    #         lang = db.Language.get(name=item.name)
    #         langs.append(lang)
    db.App(**row.dict())
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
