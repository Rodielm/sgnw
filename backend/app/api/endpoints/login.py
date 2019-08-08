
from fastapi import APIRouter
from app.api.models.user import ( UserSecurity,
    UserBase, ManyUsersInResponse, UserInResponse, UserInDB, UserInUpdate)
from datetime import timedelta
from app.crud import user as db_user
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core import config
from app.core.jwt import *
from app.core.security import *
from app.core.utils import create_aliased_response
from typing import List

from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

router = APIRouter()


@router.post("/access-token")
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = db_user.authenticate(
        email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password")
    elif not user.isActive:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/test-token")
def test_token(current_user: UserSecurity = Depends(get_current_user)):
    """
    Test access token
    """
    return current_user
