
from fastapi import APIRouter
from app.api.models.group import *
from app.crud import group as db_group
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

@router.get("/", response_model=List[GroupInResponse])
def read_groups():
    groups = db_group.read_groups()
    return groups


@router.get("/{name}",response_model=GroupInResponse)
def read_group_by_name(name: str):
    row = db_group.read_group_name(name)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Group not exist",
                            )
    return row


@router.post("/", status_code=HTTP_201_CREATED)
def create_group(group: GroupInDB):
    return db_group.create_group(group)


@router.put("/{id}")
def update_group(id:int,group: GroupInUpdate):
    row = db_group.update_group(id,group)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Group not exist",
                            )
    return row


@router.delete("/{id}")
def delete_group(id: int):
    db_group.delete_group(id)
