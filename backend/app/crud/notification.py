from typing import List
import logging
from app.api.models.notification import *
from app.api.models.NotifyState import NotifyStateInUpdate
from app.api.models.notifyUser import NotifyUserInResponse
from app.api.models.master import MasterBase
from app.db.base import *
import os
import gettext


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
def read_notification_by_user(id: int, idNoti: int = 0):
    sql_debug(True)
    notifications: List[NotifyUserInResponse] = []
    user = db.User.get(id=id)
    langDefault = 'es'

    if user.config:
        langDefault = user.config['languages']
    _ = langTranslate(langDefault)

    if idNoti is 0:
        rows = select(nu for nu in db.NotifyUser if nu.user ==
                      user and nu.status.id is not 3)[:]
    else:
        rows = select(nu for nu in db.NotifyUser if nu.user ==
                      user and nu.id == idNoti)[:]
    for row in rows:
        groups: List[GroupBase] = []
        roles: List[RoleBase] = []
        notify = row.to_dict()
        notify['notification'] = row.notification.to_dict()
        notify['notification']['summary'] = (
            _(row.notification.summary) % (row.notification.summary_args))
        notify['notification']['body'] = (
            _(row.notification.body) % (row.notification.body_args))
        notify['notification']['app'] = row.notification.app.to_dict()
        notify['status'] = row.status.to_dict()
        for g in row.recipient_groups:
            groups.append(g.to_dict())
        notify['recipient_group'] = groups
        for r in row.recipient_roles:
            roles.append(g.to_dict())
        notify['recipient_roles'] = roles
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
        body_type=row.body_type,
        hints=row.hints,
        app=app,
        I10n_vers=row.I10n_vers)
    # Compute user relationships to notifications
    notifications_by_user = {}
    # Users
    if row.users:
        users = row.users
        addUsers(users, notifications_by_user)
    # Groups
    if row.recipient_groups:
        print("Procesando grupos")
        groups = row.recipient_groups
        addGroups(groups,notifications_by_user,app)
    # Roles
    if row.recipient_roles:
        roles = row.recipient_roles
        addRoles(roles,notifications_by_user,app)
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


def addUsers(users, notifications_by_user):
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


def addGroups(groups,notifications_by_user,app):
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

def addRoles(roles,notifications_by_user,app):
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

@db_session
def update_notification_by_status(userNotifyStatus: UserNotifyStatus, current_user: int):
    # 1: Nuevo, 2: Leído, 3: Borrado
    sql_debug(True)
    notifyState = db.NotifyState.get(id=userNotifyStatus.idStatus)
    notifyuser = db.NotifyUser.get(
        id=userNotifyStatus.idNoti, user=current_user)
    if notifyuser is None:
        logging.error('This notification does not exist')
    else:
        notifyuser.status = notifyState
    commit()
    notifyUpdated = read_notification_by_user(
        current_user, userNotifyStatus.idNoti)[0]
    return notifyUpdated


@db_session
def delete_notification(id: int):
    db.Notification[id].delete()


def send_notification_email():
    return "send to email soon"


def langTranslate(language: str):
    try:
        lang = gettext.translation('messages', '.../locale', languages=['en'])
        lang.install()
        return lang.gettext
    except Exception as e:
        print('Falló por {}'.format(e))
        lang = gettext.NullTranslations()
        lang = gettext.translation('messages', fallback=True)
        return lang.gettext
