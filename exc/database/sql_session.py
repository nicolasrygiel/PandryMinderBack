#!/usr/bin/env python
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager

env = os.getenv('ENV', 'local')
SERVER = os.getenv('DB_HOST')
DATABASE = os.getenv('DB_DATABASE')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

DB_CONNECTION = f'mysql+pymysql://{USER}:{PASSWORD}@{SERVER}/{DATABASE}'

engine = create_engine(DB_CONNECTION, pool_pre_ping=True, pool_recycle=3600)

Session = scoped_session(sessionmaker(bind=engine))

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        Session.remove()