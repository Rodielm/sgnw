
from typing import List
from pony.orm import *
from app.api.models.master import *
from app.db.base import db



@db_session
def read_lang_name(name: str) -> MasterInResponse:
    row = db.Lang.get(name=name)
    if row:
        return row.to_dict()

@db_session
def read_lang() -> List[MasterInResponse]:
    langs: List[MasterInResponse] = []
    rows = select(r for r in db.Lang)[:]
    for row in rows:
        langs.append(row.to_dict())
    return langs

@db_session
def create_lang(row: MasterBase):
    db.Lang(**row.dict())
    commit()
    return row

@db_session
def update_lang(id: int, lang: MasterInUpdate):
    dblang = db.Lang.get(id=id)
    if not dblang:
        return dblang
    else:
        dblang.name = lang.name
        commit()
    return dblang

@db_session
def update_lang_status(id: int):
    sql_debug(True)
    row = db.Lang.get(id=id)
    if not row:
        return row
    else:
        row.isActive = False
    return row.to_dict()

@db_session
def delete_lang(id:int):
    db.Lang[id].delete()
    
