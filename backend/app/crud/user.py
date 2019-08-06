
from typing import List
from pony.orm import *
from app.models.user import (UserBase, UserInResponse, UserInDB, UserInUpdate)
from app.db.base import db
from app.core.security import get_password_hash, verify_password


@db_session
def get(user_id: int) -> Optional[UserInResponse]:
    return db.User.get(id=user_id)

@db_session
def is_user_active(user: UserBase):
    return "test"

@db_session
def is_user_admin(user: UserBase):
    return "test"

@db_session
def get_by_email(email: str) -> Optional[UserInResponse]:
    return db.User.get(email=email)

@db_session
def authenticate(email:str,password:str) -> Optional[UserInDB]:
    user = get_by_email(emai=email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

@db_session
def create_user(user: UserInDB):
    user = db.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        username=user.username,
        password=get_password_hash(user.password)
    )
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
def delete_user(id: int):
    db.User[id].delete()
