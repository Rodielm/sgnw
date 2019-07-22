
from fastapi import APIRouter
from app.models.app import *
from app.crud import app as db_app
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

@router.get("/", response_model=List[AppInResponse])
def read_apps():
    apps = db_app.read_apps()
    return apps


@router.get("/{name}",response_model=AppInResponse)
def read_app_by_name(name: str):
    row = db_app.read_app_for_name(name)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="App not exist",
                            )
    return row


@router.post("/", status_code=HTTP_201_CREATED)
def create_app(app: AppInDB):
    return db_app.create_app(app)


@router.put("/{id}")
def update_app(id:int, app: AppInUpdate):
    row = db_app.update_app(id,app)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="App not exist",
                            )
    return row


@router.delete("/{id}")
def delete_app(id: int):
    db_app.delete_app(id)
