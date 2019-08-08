import logging
from .base import *
from app.core.security import get_password_hash, verify_password
from app.models.notification import NotificationInCreate
from app.crud.notification import create_notification
from app.models.app import AppNotification
from app.models.group import GroupNotification
from app.models.user import UserNotification


# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db_params = {'provider': 'sqlite', 'filename': 'notify.db', 'create_db': True}


def init():
    db.bind(db_params)
    try:
        db.generate_mapping()
        # db.drop_all_tables(True)
        # logging.info("Dropping Tables completed")
    except Exception as e:
        logging.error("Dropping Tables: {}".format(e))
    logging.info("initilize database")
    try:
        # db.create_tables()
        # logging.info("populate database")
        # populate_database()
        logging.info("test queries")
        # test_query()
        test_db()
    except Exception as e:
        logging.error("Creating tables: {}".format(e))


@db_session
def test_query():
    result = select(u for u in db.User if '1' in u.groups.id)[:]
    print(result)

@db_session
def test_db():
    app = db.App.get(name='App3')
    logging.info('Prueba de este test {}'.format(AppNotification(id=app.id,app=app.name)))

    groups = select(g for g in db.Group)[:2]
    users = select(u for u in db.User)[:2]
    
    AppNoti = AppNotification(id=app.id,name=app.name)
    groupNoti: List[GroupNotification] = []
    userNoti: List[UserNotification] = []

    for group in groups:
        groupNoti.append(GroupNotification(name=group.name))

    for u in users:
        userNoti.append(UserNotification(email=u.email,username=u.username))

    noti = NotificationInCreate(
        summary='prueba de summary',
        body='prueba de body',
        app=AppNotification(id=app.id,name=app.name),
        user=userNoti,
        recipient_groups=groupNoti,
    )

    create_notification(noti)
    # g = db.Group.get(name='App3', app=app)

@db_session
def populate_database():
    
    group1 = db.Group(name='group1')
    group2 = db.Group(name='group2')

    role1 = db.Role(name='role1')
    role2 = db.Role(name='role2')

    db.Role(name='role3')

    user1 = db.User(
        username='user1',
        password=get_password_hash('1234'),
        email='fulan@gmail.com',
        groups=[group1])

    user2 = db.User(
        username='user2',
        password=get_password_hash('1234'),
        email='fulin@gmail.com',
        groups=[group1])

    user3 = db.User(
        username='user2',
        password=get_password_hash('1234'),
        email='fulint@gmail.com',
        roles=[role2])

    user4 = db.User(
        username='user2',
        password=get_password_hash('1234'),
        email='fuline@gmail.com',
        roles=[role2])

    lang1 = db.Lang(name='Spanish')
    lang2 = db.Lang(name='English')
    lang3 = db.Lang(name='French')

    state = db.NotifyState(name='Nuevo')
    db.NotifyState(name='Leido')
    db.NotifyState(name='Borrado')

    db.Group(name='group3')

    app = db.App(name='App3')
    db.App_lang(app=app, lang=lang1, filename='example.ts')

    users = [user1, user2]
    groups = [group1]
    roles = [role1]

# noti = db.Notification(
#     summary='Testing', body='Notification testing', app=app)

# users = [user1, user2]

# 1er Caso: Usuarios directos
# # By users
#     for user in users:
#         print(user)
#         db.NotifyUser(
#             notification=noti,
#             user=user,
#             status=state,
#             recipient_user=True
#         )

# # 2do Caso: Grupos
# # By Groups
# users_by_groups = select(u for u in db.User if '1' in u.groups.id)[:]

# for user in users_by_groups:
#     db.NotifyUser(
#         notification=noti,
#         user=user,
#         status=state,
#         recipient_user=False,
#         recipient_groups=group1
#     )


# # # 3er Caso: Roles
#     users_by_roles = select(u for u in db.User if '2' in u.roles.id)[:]
#     for user in users_by_roles:
#         db.NotifyUser(
#             notification=noti,
#             user=user,
#             status=state,
#             recipient_user=False,
#             recipient_roles=role2
#         )

# # 4to Caso: Todos
#     # Groups and roles separated and then users alone
#     users_by_groups = select(u for u in db.User if '1' in u.groups.id)[:]
#     users_by_roles = select(u for u in db.User if '1' in u.roles.id)[:]

#     for user in users_by_roles:
#         db.NotifyUser(
#             notification=noti,
#             user=user,
#             status=state,
#             recipient_user=False,
#             recipinet_groups=groups,
#             recipient_roles=roles
#         )
