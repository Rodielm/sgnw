import logging
from pony.orm import *
from . import db


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
        populate_database()
        logging.info("populate database")
    except Exception as e:
        logging.error("Creating tables: {}".format(e))


@db_session
def populate_database():
    db.User(first_name='fulano',
            last_name='fulanin',
            username='user1',
            password='1234',
            email='fulan@gmail.com')

    user2 = db.User(first_name='fulana',
                    last_name='fulanan',
                    username='user2',
                    password='1234',
                    email='fulina@gmail.com')

    lang1 = db.Lang(name='Spanish')
    lang2 = db.Lang(name='English')
    lang3 = db.Lang(name='French')

    state = db.NotifyState(name='Nuevo')
    db.NotifyState(name='Leido')
    db.NotifyState(name='Borrado')

    group1 = db.Group(name='group1')
    group2 = db.Group(name='group2')
    db.Group(name='group3')

    role1 = db.Role(name='role1')
    role2 = db.Role(name='role2')
    db.Role(name='role3')

    app = db.App(name='App3')
    db.App_lang(app=app, lang=lang1, filename='example.ts')

    #TODO NotifyUser insert by group, roles or user..
    # Cuando se inserta por usuario el recipient user será true

    # En caso de grupo o roles 
    # Como objeto se inserta NotifyUser con sus listado de roles y grupos
    # Luego se inserta todos los usuarios que pertenece al grupo tal o roles en notifyUser
    # Como se insertaría cuando solo es grupo y roles.  

    commit()
