from fastapi import APIRouter, File, Form, UploadFile
from app.api.models.app import *
from app.crud import app as db_app
from fastapi.encoders import jsonable_encoder
from app.core.utils import create_aliased_response
from typing import List
from shutil import copyfile, copyfileobj

import os
import sys

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


@router.get("/{name}", response_model=AppInResponse)
def read_app_by_name(name: str):
    row = db_app.read_app_for_name(name)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="App not exist",
                            )
    return row


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


@router.post("/upload")
async def create_upload_file(file_upload: UploadFile = File(...)):
    test_dir = "/home/rodielmj/Desktop/data"
    # base_dir = os.environ.get('LANGFILE_BASEDIR', None)
    # dir_list = os.environ.get('LANGFILE_DIRLIST', "")
    filepath = os.path.join(test_dir, file_upload.filename)
    print('directory paste: {}'.format(filepath))
    try:
        # contents = file_upload.file.read()
        # print('contents size {}'.format(len(contents)))
        # with open(filepath, 'wb') as out_file:
        #     copyfileobj(file_upload.file, out_file)
        contents = await file_upload.read()
        with open(contents, 'rb') as f_in, open(filepath, 'wb') as f_out:
            copyfileobj(f_in, f_out)
    except Exception as e:
        print('An exception occurred {}'.format(e))
    # print('dir_list: {}'.format(dir_list))
    # if (base_dir is None) or (os.path.isdir(base_dir) is False):
    #     eprint("LANGFILE_BASEDIR='{}' is not a directory".format(base_dir))
    return {"filename ": file_upload.filename}


@router.post("/files")
async def create_file(
    file: bytes = File(...),
    fileb: UploadFile = File(...),
    token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }


@router.post("/", status_code=HTTP_201_CREATED)
def create_app(app: AppCreate):
    return db_app.create_app(app)


@router.put("/{id}")
def update_app(id: int, app: AppInUpdate):
    row = db_app.update_app(id, app)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="App not exist",
                            )
    return row


@router.delete("/{id}")
def delete_app(id: int):
    db_app.delete_app(id)


@router.delete("/{idApp}/lang/{idLang}")
def delete_applang(idApp: int, idLang: int):
    db_app.delete_applang(idApp, idLang)
