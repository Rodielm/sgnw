import logging
from .base import *

# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db_params = {'provider': 'sqlite', 'filename': 'notify.db', 'create_db': True}


def init():
    db.bind(db_params)
    try:
        db.generate_mapping()
        db.drop_all_tables(True)
        logging.info("Dropping Tables completed")
    except Exception as e:
        logging.error("Dropping Tables: {}".format(e))
    logging.info("initilize database")
    try:
        db.create_tables()
        logging.info("populate database")
        populate_database()
        logging.info("test queries")
        # test_query()
    except Exception as e:
        logging.error("Creating tables: {}".format(e))


@db_session
def test_query():
    result = select(u for u in db.User if '1' in u.groups.id)[:]
    print(result)


@db_session
def populate_database():

    group1 = db.Group(name='group1')
    group2 = db.Group(name='group2')

    user1 = db.User(
        first_name='fulano',
        last_name='fulanin',
        username='user1',
        password='1234',
        email='fulan@gmail.com',
        groups=[group1])

    user2 = db.User(
        first_name='fulana',
        last_name='fulanan',
        username='user2',
        password='1234',
        email='fulina@gmail.com',
        groups=[group1])

    user3 = db.User(
        first_name='miguel',
        last_name='fulanan',
        username='user2',
        password='1234',
        email='fulina@gmail.com',
        groups=[group2])

    user4 = db.User(
        first_name='mario',
        last_name='fulanan',
        username='user2',
        password='1234',
        email='fulina@gmail.com',
        groups=[group2])

    lang1 = db.Lang(name='Spanish')
    lang2 = db.Lang(name='English')
    lang3 = db.Lang(name='French')

    state = db.NotifyState(name='Nuevo')
    db.NotifyState(name='Leido')
    db.NotifyState(name='Borrado')

    db.Group(name='group3')

    role1 = db.Role(name='role1')
    role2 = db.Role(name='role2')
    db.Role(name='role3')

    app = db.App(name='App3')
    db.App_lang(app=app, lang=lang1, filename='example.ts')

    # noti = db.Notification(
    #     summary='Testing', body='Notification testing', app=app)

    # users = [user1, user2]
    # groups = [group1]
    # roles = [role1]


# # 1er Caso: Usuarios directos
# # By users
# #     for user in users:
# #         print(user)
# #         db.NotifyUser(
# #             notification=noti,
# #             user=user,
# #             status=state,
# #             recipient_user=True
# #         )

# # 2do Caso: Grupos
# # By Groups

#     users_by_groups = select(u for u in db.User if '1' in u.groups.id)[:]

#     for user in users_by_groups:
#         db.NotifyUser(
#             notification=noti,
#             user=user,
#             status=state,
#             recipient_user=False,
#             recipient_groups=group1
#         )


# # 3er Caso: Roles

#     users_by_roles = select(u for u in db.User if '1' in u.roles.id)[:]

#     for user in users_by_roles:
#         db.NotifyUser(
#             notification=noti,
#             user=user,
#             status=state,
#             recipient_user=False,
#             recipient_roles=group1
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
