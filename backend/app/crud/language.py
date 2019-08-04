
from typing import List
from pony.orm import *
from app.models.master import *
from app.db.base import db



@db_session
def read_lang_name(name: str) -> MasterInResponse:
    row = db.Language.get(name=name)
    if row:
        return row.to_dict()

@db_session
def read_lang() -> List[MasterInResponse]:
    langs: List[MasterInResponse] = []
    rows = select(r for r in db.Language)[:]
    for row in rows:
        langs.append(row.to_dict())
    return langs

@db_session
def create_lang(row: MasterBase):
    db.Language(**row.dict())
    commit()
    return row

@db_session
def update_lang(id: int, lang: MasterInUpdate):
    dblang = db.Language.get(id=id)
    if not dblang:
        return dblang
    else:
        dblang.name = lang.name
        commit()
    return dblang

@db_session
def delete_lang(id:int):
    db.Language[id].delete()
    
