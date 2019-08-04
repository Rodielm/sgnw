
from typing import List
from pony.orm import *
from app.models.rol import (RoleBase,RoleInUpdate,RoleInResponse,RoleInDB)
from app.db.base import db


@db_session
def create_rol(row: RoleBase):
    db.Role(**row.dict())
    commit()
    return row


@db_session
def update_rol(id: int, rol: RoleInUpdate):
    dbrol = db.Role.get(id=id)
    if not dbrol:
        return dbrol
    else:
        dbrol.name = rol.name
        commit()
    return dbrol


@db_session
def read_roles() -> List[RoleInResponse]:
    roles: List[UserInResponse] = []
    rows = select(r for r in db.Role)[:]
    for row in rows:
        roles.append(row.to_dict())
    return roles


@db_session
def read_role_name(name: str) -> RoleInResponse:
    row = db.Role.get(name=name)
    if row:
        return row.to_dict()

@db_session
def delete_role(id:int):
    db.Role[id].delete()
    
