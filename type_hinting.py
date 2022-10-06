# NamedTuple
from typing import NamedTuple, TypedDict
from typing import Dict


class User(NamedTuple):
	name: str
	age: int


user = User("Maks", 19)
print(user.age)
# user.age = 20   # can't set attribute


# TypedDict
class User(TypedDict):
	name: str
	age: int


print(User(name="Maks", age=19)["name"])


# Dict
def get_gps_coordinates() -> Dict[str, float]:
	return {"long": 10.0, "lat": 10.0}


print(get_gps_coordinates()[1])


# Literal
