
from typing import List
from pony.orm import *
from app.api.models.group import *
from app.db.base import db


@db_session
def read_groups():
    groups: List[GroupInResponse] = []
    rows = select(g for g in db.Group if g.isActive == True)
    for row in rows:
        group = row.to_dict()
        if row.app is not None:
            group['app'] = row.app.to_dict()
        groups.append(group)
    return groups


@db_session
def read_group_name(name: str) -> GroupInResponse:
    row = db.Group.get(name=name)
    if row:
        group = row.to_dict()
        group['app'] = row.app.to_dict()
        return group


@db_session
def create_group(row: GroupBase):
    app = None
    if row.app:
        app = db.App.get(name=row.app.name)
    db.Group(name=row.name, description=row.description, app=app)
    return row


@db_session
def update_group(id: int, group: GroupInUpdate):
    dbgroup = db.Group.get(id=id)
    if not dbgroup:
        return dbgroup
    else:
        if group.name is not None:
            dbgroup.name = group.name
        if group.description is not None:
            dbgroup.description = group.description
    return dbgroup


@db_session
def update_group_status(id: int):
    sql_debug(True)
    group = db.Group.get(id=id)
    if not group:
        return group
    else:
        group.isActive = False
    return group.to_dict()


@db_session
def delete_group(id: int):
    db.group[id].delete()
