
from typing import List
from pony.orm import *
from app.models.notification import *
from app.models.master import MasterBase
from app.db.base import db


@db_session
def read_notifications() -> List[NotificationInResponse]:
    # apps: List[AppInResponse] = []
    # rows = select(r for r in db.App)[:]
    # for row in rows:
    #     apps.append(row.to_dict())
    return "En construcción"


@db_session
def read_notification_for_user(name: str) -> AppInResponse:
    # row = db.App.get(name=name)
    # if row:
    #     return row.to_dict()
    return "En construcción"


@db_session
def create_notification(row: NotificationInCreate):
    status = db.NotifyState.get(id=1)
    # Create Notification
    Notify = db.Notification(
        summary=row.summary,
        summary_args=row.summary_args,
        body=row.body,
        body_args=row.body_args,
        hints=row.hints,
        app=row.app,
        I10n_vers=row.I10n_vers)
    # By User direct
    if row.user:
        for users in row.user:
            # Looking for user
            user = db.User(id=users.id)
            db.NotifyUser(
                notification=Notify,
                user=user,
                status=status,
                recipient_user=True
            )
        # By Groups
    if row.recipient_groups:
        # Looking for groups
        for groups in row.recipient_groups:
            user_by_groups = select(
                u for u in db.User if groups.id in u.groups.id)[:]
            for user in user_by_groups:
                db.NotifyUser(
                    notification=Notify,
                    user=user,
                    status=status,
                    recipient_user=False,
                    recipient_groups=[row.recipient_groups]
                )
        # By Roles
        if row.recipient_roles:
            # Looking for roles
            for roles in row.recipient_roles:
                user_by_roles = select(
                    u for u in db.User if roles.id in u.roles.id)[:]
            for user in user_by_roles:
                db.NotifyUser(
                    notification=Notify,
                    user=user,
                    status=status,
                    recipient_user=False,
                    recipient_roles=[row.recipient_roles]
                )
    return Notify


@db_session
def delete_notification(id: int):
    db.app[id].delete()
