from typing import NamedTuple, TypedDict, Optional, \
                Union, Iterable, List, Sequence, MutableSequence, \
                Mapping, Callable
from dataclasses import dataclass
import enum


# NamedTuple - Simple Structure, but without setting attributes
class User(NamedTuple):
    name: str
    age: int


user = User("Maks", 19)
print(user.age)
# user.age = 20   # can't set attribute


# TypedDict - Simple Structure, but getting element with key, like dictionary ds
class User(TypedDict):
    name: str
    age: int


user = User(name="Maks", age=19)
print(user["name"])
# user["name"] = "Max"


# Dataclass - Simple Structure
@dataclass
class User:
    name: str
    age: int


user = User("Maks", 19)
print(user.name)
# user.name = "Max"


# Dataclass as NamedTuple
@dataclass(frozen=True)
class User:
    name: str
    age: int


user = User("Maks", 19)
print(user.name)
# user.name = 20   # can't set attribute


# NOTE: NamedTuple useful in unpacking case. In other case, dataclass is more useful, also it gets less memory than
# namedtuple Even if you are going to use smth like tuple without unpacking cases, use dataclass with frozen and
# slots are True.


# Enum - Simple Structure, but with ability to iterate
# Useful in case to save parameters, statuses of something
class TaskStatuses(enum.Enum):
    to_do = 1
    doing = 2
    done = 3


for task_status in TaskStatuses:
    print(task_status)
    print(task_status.value)
    print(task_status.name)

print(TaskStatuses.to_do.name, TaskStatuses.to_do.value)


# Unique Enum Elements
@enum.unique
class UniqueTaskStatus(enum.Enum):
    to_do = 1
    doing = 2
    done = 3

    # done = 4  # Here will be occurred an error


# IntEnum - Simple Structure, but with ability to iterate and to comparison an elements, which supports comparison
# with values
class TaskStatuses(enum.IntEnum):
    done = 3
    doing = 2
    to_do = 1


print(sorted(TaskStatuses))


# Example of the USING INTERFACE.
# Difference between interface and abstract class is,
# abstract class contains implementation of the methods, but interface doesn't contain an implementation
# GOALS of them, to show what methods and attributes must be in their child classes
@dataclass(frozen=True)
class Weather:
    temperature: Optional[int]


class WeatherStorage:
    """Interface for any storage saving Weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage(WeatherStorage):
    def save(self, weather: Weather) -> None:
        print("Implementation of the plain text weather storage...")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)


save_weather(Weather(temperature=1), PlainFileWeatherStorage())


# MYPY:
# 1. install
# 2. use by "mypy code.py"
# 3. see errors


# Optional, Union
# Optional -> data: DataType | None  # that means, type of the data var is DataType OR None
# Union -> data: DataType1 | DataType2  # that means, type of the data var can be DataType1 or DataType2
@dataclass
class User:
    name: Optional[str] = "Maks"  # "Maks" is default value of the attr
    age: Union[int, float] = 19  # 19 is default value of the attr


print(User(name=None, age=1.5))
print(User().name)
print(User().age)


# Iterable - it's type that can contain any iterable data structure (list, set, tuple)
# If you have iterable algorithm, use Iterable instead of list, set, tuple, etc.
# Otherwise, the algorithm will be depended on concrete data structure in order to perform
def sort_users_by_age_ascending(users: Iterable[User]) -> List:
    return sorted(users, key=lambda x: x.age)


print(sort_users_by_age_ascending([User("Max", 20), User("Maks", 19)]))
print(sort_users_by_age_ascending((User("Max", 20), User("Maks", 19))))


# Sequence - it's type that can contain any data structure that supports getting element by index
# If you have function that works with some collection by indexing, use Sequence instead of list, set, tuple, etc.
# Otherwise, function will be depended on concrete obj type in order to perform
def get_youngest_user(users: Sequence[User]) -> User:
    sorted_users = sorted(users, key=lambda x: x.age)
    return sorted_users[0]


print(get_youngest_user([User("Max", 20), User("Maks", 19)]))
print(get_youngest_user((User("Max", 20), User("Maks", 19))))


# MutableSequence - it's like Sequence, but with one additional difference.
# By MutableSequence you can set value to elements, except tuple's element
def set_youngest_user_age_to_0_and_get_it(users: MutableSequence[User]) -> User:
    sorted_users = sorted(users, key=lambda x: x.age)
    sorted_users[0].age = 0
    return sorted_users[0]


print(set_youngest_user_age_to_0_and_get_it([User("Max", 20), User("Maks", 19)]))
# print(set_youngest_user_age_to_0_and_get_it((User("Max", 20), User("Maks", 19))))
# To give tuple is not correct because tuple is immutable type


# Mapping - it's type that can contain dict, UserDict, default dict, OrderedDict, ChainMap. Mapping also like Iterable
# and Sequence/MutableSequence Types, use Mapping in order to not make any parameter/var/attr depended on concrete
# obj type
def smth(some_users: Mapping[str, User]) -> None:
    print(some_users["alex"])
    some_users["alex"].name = "Sula"


user_dict = {
    "alex": User(name="Max", age=20),
    "petr": User(name="Maks", age=19)
}
smth(user_dict)
print(user_dict)  # OUTPUT: {'alex': User(name='Sula', age=20), 'petr': User(name='Maks', age=19)}


# Callable - it's type that can contain function/class, all callable objects.
# Function in Python is just a object. So you can give function as argument to function parameter
# Use Callable if you want to give function as argument to function parameter
def sum_a_and_b(a: int, b: int) -> int:
    return a + b


def my_sum(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)


print(my_sum(sum_a_and_b, 1, 2))


# Stub Files - It's file where you can set type hinting to any Python code.
# For example, you are using external package, but in that package is not used type hinting.
# And you want to set type hinting to package. You can set by Stub files.

# Step 1. Create .pyi file with module name. Example: utils.py -> stub file for that file must be utils.pyi
# Step 2. Rewrite function that you want to set type hinting.
# Tip: In order to not rewrite whole function you can write just ... in the function block, then by this
# You can set just input/output type hinting

# utils.py
# def my_sum(a, b):
#     return a + b

# utils.pyi
# def my_sum(a: int, b: int) -> int: ...
# or
# def my_sum(a: int, b: int) -> int:
#     return a + b
