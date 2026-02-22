from sqlalchemy.inspection import inspect
from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    def __repr__(self) -> str:
        output = f"id : {self.id}"
        table_columns = inspect(type(self)).c
        if "id_str" in table_columns:
            output += f", id_str : {self.id_str}"
        if "name" in table_columns:
            output += f", name : {self.name}"
        return output
            
    def to_dict(self, excluded=[]):
        obj = {}
        table_columns = inspect(type(self)).c
        for column in table_columns:
            if column.name not in excluded:
                obj[column.name] = getattr(self, column.name)
        return obj
    