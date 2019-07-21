
from typing import List
from pony.orm import *
from app.models.group import *
from app.db.base import db


@db_session
def read_groups() -> List[GroupInResponse]:
    groups: List[GroupInResponse] = []
    rows = select(r for r in db.Group)[:]
    for row in rows:
        groups.append(row.to_dict())
    return groups


@db_session
def read_group_name(name: str) -> GroupInResponse:
    row = db.Group.get(name=name)
    if row:
        return row.to_dict()


@db_session
def create_group(row: GroupBase):
    db.Group(**row.dict())
    commit()
    return row


@db_session
def update_group(id: int, group: GroupInUpdate):
    dbgroup = db.Group.get(id=id)
    if not dbgroup:
        return dbgroup
    else:
        dbgroup.name = group.name
        commit()
    return dbgroup


@db_session
def delete_group(id: int):
    db.group[id].delete()
