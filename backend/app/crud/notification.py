from typing import List
import logging
from app.api.models.notification import *
from app.api.models.NotifyState import NotifyStateInUpdate
from app.api.models.master import MasterBase
from app.db.base import *


@db_session
def read_notification_for_user(id: int):
    sql_debug(True)
    notify: List[NotificationInResponse] = []
    rows = select(
        n for n in db.Notification
        if id in n.notify_users.user.id)[:]
    for row in rows:
        notify.append(row.to_dict())
    return notify


@db_session
def read_notification_by_user(id: int):
    sql_debug(True)
    notifications = []
    user = db.User.get(id=id)
    rows = select(nu for nu in db.NotifyUser if nu.user == user)[:]
    for row in rows:
        groups = []
        roles = []
        notify = row.to_dict()
        notify['notification'] = row.notification.to_dict()
        notify['status'] = row.status.to_dict()
        for g in row.recipient_groups:
            groups.append(g.to_dict())
        notify['groups'] = groups
        for r in row.recipient_roles:
            roles.append(g.to_dict())
        notify['roles'] = roles
        notifications.append(notify)
    return notifications


@db_session
def create_notification(row: NotificationInCreate):
    sql_debug(True)
    status = db.NotifyState.get(id=1)
    app = db.App.get(id=row.app.id)
    print("Inserting notification")
    # Create Notification
    Notify = db.Notification(
        summary=row.summary,
        summary_args=row.summary_args,
        body=row.body,
        body_args=row.body_args,
        hints=row.hints,
        app=app,
        I10n_vers=row.I10n_vers)
    # Compute user relationships to notifications
    notifications_by_user = {}
    # Users
    if row.users:
        users = row.users
        for u in users:
            user = db.User.get(username=u.username)
            if user is None:
                user = db.User.get(email=u.email)
            if user is None:
                logging.error(
                    'User doest not exist {}'.format(u))
                continue
            uid = user.id
            notifications_by_user[uid] = {}
            notifications_by_user[uid]['recipient_user'] = True
            notifications_by_user[uid]['recipient_groups'] = set()
            notifications_by_user[uid]['recipient_roles'] = set()
    # Groups
    if row.recipient_groups:
        print("Procesando grupos")
        groups = row.recipient_groups
        for gr in groups:
            group = db.Group.get(name=gr.name, app=app)
            if group is None:
                group = db.Group.get(name=gr.name, app=None)
            if group is None:
                logging.error('Group doest not exist {}'.format(gr.to_dict()))
                continue
            for user in group.users:
                uid = user.id
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
                logging.error('Roles doest not exist {}'.format(ro.to_dict()))
                continue
            for user in role.users:
                uid = user.id
                if uid not in notifications_by_user:
                    notifications_by_user[uid] = {}
                    notifications_by_user[uid]['recipient_user'] = False
                    notifications_by_user[uid]['recipient_groups'] = set()
                    notifications_by_user[uid]['recipient_roles'] = set()
                notifications_by_user[uid]['recipient_roles'].add(role)
    # Create NotifyUser entries
    new_state = db.NotifyState.get(name='Nuevo')
    for uid in notifications_by_user:
        user = db.User.get(id=uid)
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
def update_notification_by_status(idNotification: int, idUser: int, notifystate: NotifyStateInUpdate):
    # FIXME change idUser by current_user logged
    # 1: Nuevo, 2: Leído, 3: Borrado
    notifyState = db.NotifyState.get(name=notifystate.name)
    notifyuser = db.NotifyUser.get(notification=idNotification, user=idUser)
    if notifyuser is None:
        logging.error('This notification does not exist')
    else:
        notifyuser.status = notifyState


@db_session
def delete_notification(id: int):
    db.Notification[id].delete()


def send_notification_email():
    return "send to email soon"
