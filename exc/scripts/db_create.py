### Std Imports
import os

### Lib Imports
from dotenv import load_dotenv, find_dotenv
env_file = find_dotenv(
    "/Users/nicolasrygiel/work/pandryminder/PandryMinderBack/exc/.env"
)
load_dotenv(env_file) # Vars loaded before imports because of db format

### Mycode Imports
from database.sql_session import session_scope, engine
from models.base_model import BaseModel

# Models Imports, used due to metadata create all
from models.test import TestTable

### Code
def create_all_tables():
    with session_scope() as dbSession:
        BaseModel.metadata.create_all(engine)
        dbSession.commit()

### Main
if __name__ == "__main__":
    create_all_tables()