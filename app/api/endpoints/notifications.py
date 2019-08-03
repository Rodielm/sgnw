
from fastapi import APIRouter
from app.models.notification import *
from app.crud import notification as db_noti
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

@router.get("/{user}", response_model=List[NotificationInResponse])
def read_notification_user():
    #TODO  Read Notification by Current user
    return "User Notification list"


@router.post("/", status_code=HTTP_201_CREATED)
def create_notification(notification: NotificationInCreate):
    # app, notify users, user, groups, roles list and status
    return db_noti.create_notification(notification)


@router.delete("/{id}")
def delete_notification(id: int):
    # TODO delete notification by user
    db_noti.delete_notification(id)
