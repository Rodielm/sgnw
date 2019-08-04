
from fastapi import APIRouter
from app.models.user import (UserBase, ManyUsersInResponse, UserInResponse, UserInDB, UserInUpdate)
from app.crud import user as db_user
from fastapi.encoders import jsonable_encoder
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

@router.get("/", response_model=List[UserInResponse])
def read_users():
    users_data = db_user.findAll_users()
    return users_data


@router.get("/{email}",response_model=UserInResponse)
def find_user_by_email(email: str):
    user = db_user.read_user_email(email)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not exist",
                            )
    return user


@router.post("/", status_code=HTTP_201_CREATED)
def create_user(user: UserInDB):
    return db_user.create_user(user)


@router.put("/{id}")
def update_user(id:int,user: UserInUpdate):
    user = db_user.update_user(id,user)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="User not exist",
                            )
    return user


@router.delete("/{id}")
def delete_user(id: int):
    db_user.delete_user(id)
