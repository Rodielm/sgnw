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
            email='fulan@gmail.com')

    db.User(first_name='fulana',
            last_name='fulanan',
            email='fulina@gmail.com')
    db.Language(name='Spanish')
    db.Language(name='English')
    db.Language(name='French')
    commit()
