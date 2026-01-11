from datetime import datetime

from sqlalchemy.inspection import inspect
from sqlalchemy import desc, exc, func, select, update, delete

from database.sql_session import session_scope
from models.test import TestTable

class TestEntity():
  # -- GET LIST --
  @staticmethod
  def get_test_list():
    with session_scope() as db_session: 
        output =[]
        stmt = select(TestTable)
        elts = db_session.execute(stmt)
        for elt, in elts:
           output.append({
              "id": elt.id,
              "name": elt.name
           })
        return output
    
