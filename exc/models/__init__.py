from sqlalchemy.orm import declarative_base

Base = declarative_base() # model base class
from .base_model import BaseModel
from .ingredient import *
from .recipe import *
from .test import *