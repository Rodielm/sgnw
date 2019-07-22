
from typing import List
from pony.orm import *
from app.models.user import (UserBase, UserInResponse, UserInDB, UserInUpdate)
from app.db.base import db


@db_session
def create_user(user: UserBase):
    db.User(**user.dict())
    commit()
    return user


@db_session
def update_user(id: int, user: UserInUpdate):
    dbuser = db.User.get(id=id)
    if not dbuser:
        return dbuser
    else:
        dbuser.first_name = user.first_name
        dbuser.last_name = user.last_name
        dbuser.email = user.email
        dbuser.username = user.username
        commit()
    return dbuser


@db_session
def findAll_users() -> List[UserInResponse]:
    users: List[UserInResponse] = []
    rows = db.User.select()
    for row in rows:
        users.append(row.to_dict())
    return users


@db_session
def read_user_email(email: str) -> UserInResponse:
    # row = db.User.select_by_sql('select * from user p where p.email = $email')[:1]
    row = db.User.get(email=email)
    if row:
        return row.to_dict()

@db_session
def delete_user(id:int):
    db.User[id].delete()
    
