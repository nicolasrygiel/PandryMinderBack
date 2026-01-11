from enum import IntEnum

class BaseEnum(IntEnum):

  @classmethod
  def _missing_(cls, value: int):
    # create a new instance of the enum with the given value
    # and set the name to None even if value is not part of the enum
    obj = int.__new__(cls)
    obj._name_ = None
    obj._value_ = value
    return obj
  
  @classmethod
  def contains(cls, other: Union[Self, int, str]) -> bool:
    # Utility method to check if a value is part of the Enum
    if other is None:
      return False
    elif isinstance(other, int):
      return other in {member.value for member in cls.__members__.values()}
    elif isinstance(other, str):
      return other.upper() in cls.__members__
    else:
      return other in cls

  @classmethod
  def get_by_name(cls, name: str) -> Union[Self, None]:
    """Returns the enum member by its name."""
    if name.upper() in cls.__members__:
      return cls[name.upper()]
    return None

  @DynamicClassAttribute
  # DynamicClassAttribute is a decorator that allows you to define a class attribute
  # that is computed dynamically when accessed.
  def name(self) -> str:
    if self._name_ is None:
      return None
    return self._name_.lower()

  def dict(self) -> dict:
    """Returns a dictionary representation of the enum instance."""
    return {'id': self.value, 'name': self.name}