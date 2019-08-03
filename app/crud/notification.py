
from typing import List
from app.models.notification import *
from app.models.master import MasterBase
from app.db.base import *


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
    sql_debug(True)
    status = db.NotifyState.get(id=1)
    app = db.App.get(id=row.app.id)

    # Create Notification
    Notify = db.Notification(
        summary=row.summary,
        summary_args=row.summary_args,
        body=row.body,
        body_args=row.body_args,
        hints=row.hints,
        app=app,
        I10n_vers=row.I10n_vers)

    # By User direct
    if row.user:
        create_notification_user(Notify, status, row)

    # By Groups
    if row.recipient_groups:
        create_notification_group(Notify, status, row)

    # By Roles
    if row.recipient_roles:
        create_notification_role(Notify, status, row)
    
    return Notify


@db_session
def delete_notification(id: int):
    db.app[id].delete()


def create_notification_user(Notify: NotificationBase, status: NotifyStateBase, row: NotificationInCreate):
    for users in row.user:
            # Looking for user
        user = db.User.get(id=users.id)
        db.NotifyUser(
            notification=Notify,
            user=user,
            status=status,
            recipient_user=True
        )


def create_notification_group(Notify: NotificationBase, status: NotifyStateBase, row: NotificationInCreate):
    groups: List[GroupNotification] = []
    for item in row.recipient_groups:
        g = db.Group.get(id=item.id)
        groups.append(g)
        # Looking for groups
    for group in groups:
        user_by_groups = select(
            u for u in db.User if group.id in u.groups.id)[:]
        for user in user_by_groups:
            db.NotifyUser(
                notification=Notify,
                user=user,
                status=status,
                recipient_user=False,
                recipient_groups=group
            )


def create_notification_role(Notify: NotificationBase, status: NotifyStateBase, row: NotificationInCreate):
    roles: List[RoleNotification] = []
    for item in row.recipient_roles:
        r = db.Role.get(id=item.id)
        roles.append(r)
    # Looking for roles
    for rol in roles:
        user_by_roles = select(
            u for u in db.User if rol.id in u.roles.id)[:]
    for user in user_by_roles:
        db.NotifyUser(
            notification=Notify,
            user=user,
            status=status,
            recipient_user=False,
            recipient_roles=rol
        )

def send_notification_email():
    return "send to email"