
from typing import List
from pony.orm import *
from app.api.models.user import (
    UserBase, UserSecurity, UserInResponse, UserInDB, UserInUpdate)
from app.db.base import db
from app.core.security import get_password_hash, verify_password


@db_session
def get(user_id: int):
    return db.User.get(id=user_id)


@db_session
def is_user_active(user: UserSecurity):
    return user.isActive


@db_session
def is_user_admin(user: UserSecurity):
    return user.isAdmin


@db_session
def get_by_email(email: str):
    return db.User.get(email=email)


@db_session
def authenticate(email: str, password: str):
    user = get_by_email(email=email)

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    print("authenticated user: {} ".format(user.to_dict()))
    return user


@db_session
def create_user(user: UserInDB):
    user = db.User(
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
        if user.username is not None:
            dbuser.username = user.username
        if user.email is not None:
            dbuser.email = user.email
    return dbuser


@db_session
def findAll_users() -> List[UserInResponse]:
    users: List[UserInResponse] = []
    rows = db.User.select()
    for row in rows:
        user = row.to_dict()
        users.append(user)
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
