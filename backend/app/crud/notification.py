from typing import List
from app.models.notification import *
from app.models.master import MasterBase
from app.db.base import *

# TODO buscar como saber si es por grupo , roles o directos
# recibiendo parametro como id grupo y roles del usuario.
# read notification by user


@db_session
def read_notification_for_user(id: int):
    sql_debug(True)
    notify: List[NotificationInResponse] = []
    # rows = select(n for n in db.Notification if JOIN(
    #     id in n.notify_users.user.id))[:]
    rows = select(n for n in db.Notification
                  if id in n.notify_users.user.id)[:]
    for row in rows:
        notify.append(row.to_dict())
    return notify


@db_session
def create_notification(row: NotificationInCreate):
    sql_debug(True)
    status = db.NotifyState.get(id=1)
    app = db.App.get(id=row.app.id)
    # Create Notification
    Notify = db.Notification(summary=row.summary,
                             summary_args=row.summary_args,
                             body=row.body,
                             body_args=row.body_args,
                             hints=row.hints,
                             app=app,
                             I10n_vers=row.I10n_vers)
    # Compute user relationships to notifications
    notications_by_user = {}
    # Users
    if row.user:
        users = row.user  # FIXME: user is a list... rename to users
        for u in users:
            user = db.User.get(username=u.username)
            if user is None:
                user = db.User.get(email=u.email)
            if user is None:
                # FIXME: Report that the user does not exist (i.e. on the
                # application error log)
                continue
            uid = u.id
            notifications_by_user[uid] = {}
            notifications_by_user[uid]['recipient_user'] = True
            notifications_by_user[uid]['recipient_groups'] = set()
            notifications_by_user[uid]['recipient_roles'] = set()
    # Groups
    if row.recipient_groups:
        groups = row.recipient_groups
        for gr in groups:
            group = db.Group.get(id=gr.name, app=app)
            if group is None:
                group = db.Group.get(name=gr.name, app=None)
            if group is None:
                # FIXME: Report that the group does not exist (i.e. on the
                # application error log)
                continue
            for u in group.users:
                uid = u.id
                if uid not in notifications_by_user:
                    notifications_by_user[uid] = {}
                    notifications_by_user[uid]['recipient_user'] = False
                    notifications_by_user[uid]['recipient_groups'] = set()
                    notifications_by_user[uid]['recipient_roles'] = set()
                notifications_by_user[uid]['recipient_groups'].add(group)
    # Roles
    if row.recipient_roles:
        roles = row.recipient_roles
        for ro in roles:
            role = db.Role.get(name=ro.name, app=app)
            if role is None:
                role = db.Role.get(name=ro.name, app=None)
            if role is None:
                # FIXME: Report that the role does not exist (i.e. on the
                # application error log)
                continue
            for u in role.users:
                uid = u.id
                if uid not in notifications_by_user:
                    notifications_by_user[uid] = {}
                    notifications_by_user[uid]['recipient_user'] = False
                    notifications_by_user[uid]['recipient_groups'] = set()
                    notifications_by_user[uid]['recipient_roles'] = set()
                notifications_by_user[uid]['recipient_roles'].add(role)
    # Create NotifyUser entries
    new_state = db.NotifyState.get(name='Nuevo')
    for uid in notifications_by_user:
        user = db.User.get(uid)
        nu = db.NotifyUser(
            notification=Notify,
            user=user,
            status=new_state,
            recipient_user=notifications_by_user[uid]['recipient_user'],
            recipient_groups=list(
                notifications_by_user[uid]['recipient_groups']),
            recipient_roles=list(
                notifications_by_user[uid]['recipient_roles']),
        )
    return Notify


@db_session
def delete_notification(id: int):
    db.Notification[id].delete()


def send_notification_email():
    return "send to email soon"
