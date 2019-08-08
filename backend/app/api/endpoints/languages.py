
from fastapi import APIRouter
from app.api.models.master import *
from app.crud import language as db_lang
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

@router.get("/", response_model=List[MasterInResponse])
def read_lang():
    return db_lang.read_lang()


@router.get("/{name}",response_model=MasterInResponse)
def read_lang_by_name(name: str):
    row = db_lang.read_lang_name(name)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Lang not exist",
                            )
    return row


@router.post("/", status_code=HTTP_201_CREATED)
def create_lang(lang: MasterInDB):
    return db_lang.create_lang(lang)


@router.put("/{id}")
def update_lang(id:int,lang: MasterInUpdate):
    row = db_lang.update_lang(id,lang)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Lang not exist",
                            )
    return row


@router.delete("/{id}")
def delete_lang(id: int):
    db_lang.delete_lang(id)
