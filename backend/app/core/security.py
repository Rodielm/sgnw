import bcrypt
import jwt
from passlib.context import CryptContext


from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from starlette.status import HTTP_403_FORBIDDEN

from app.core import config
from app.core.jwt import ALGORITHM
from app.models.token import TokenPayload
from app.db.base import db
from app.crud import user as db_user
from app.models.user import UserSecurity
from pony.orm import *

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/login/access-token")

def generate_salt():
    return bcrypt.gensalt().decode()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

@db_session
def get_current_user(token: str = Security(reusable_oauth2)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = db.User.get(id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(current_user: UserSecurity = Security(get_current_user)):
    if not current_user.isActive:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(current_user: UserSecurity = Security(get_current_user)):
    if not current_user.isAdmin:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user