
from fastapi import APIRouter, Depends
from app.api.models.notification import *
from app.core.security import get_current_active_user
from app.crud import notification as db_noti
from fastapi.encoders import jsonable_encoder
from app.core.utils import create_aliased_response
from typing import List

from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

router = APIRouter()


@router.get("/me")
def read_notification_by_user(
    current_user: UserSecurity = Depends(get_current_active_user)
):
    return db_noti.read_notification_by_user(current_user.id)


@router.post("/", status_code=HTTP_201_CREATED)
def create_notification(notification: NotificationInCreate):
    # app, notify users, user, groups, roles list and status
    return db_noti.create_notification(notification)


@router.put("/", status_code=HTTP_202_ACCEPTED)
def update_notification(current_user: int, idNotification: int, idStatus: int):
    return db_noti.update_notification_by_status(idNotification, current_user, idStatus)


@router.delete("/{id}")
def delete_notification(id: int):
    # TODO delete notification by user
    db_noti.delete_notification(id)
