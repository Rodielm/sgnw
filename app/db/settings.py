import logging
from pony.orm import *
from app.models import db


# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db_params = {'provider': 'sqlite', 'filename': 'notify.db', 'create_db': True}


def init():
    db.bind(db_params)
    sql_debug(True)
    db.generate_mapping(create_tables=True)
    logging.info("initilize database")
    try:
        populate_database()
        logging.info("populate database")
    except Exception as e:
        logging.error(e)

@db_session
def populate_database():
    u1 = db.User(first_name='fulano',
                 last_name='fulanin',
                 email='fulan@gmail.com')

    commit()

    u2 = db.User(first_name='fulana',
                 last_name='fulanan',
                 email='fulina@gmail.com')

    commit()
