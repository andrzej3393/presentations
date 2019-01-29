from dataclasses import dataclass
from typing import List


@dataclass
class User:
    username: str
    age: int


@dataclass
class Group:
    members: List[User]
    name: str


# user_a = User(username='user_a', age=20)
# user_b = User(username='user_b', age=32)
#
# group = Group([user_a, user_b], 'some_group')
#
# group.members[0].username.upper()
