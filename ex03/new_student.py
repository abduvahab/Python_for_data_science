import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ a class repersent a student"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = None
    id: str = None

    def __post_init__(self):
        message = "Student.__init__() got an unexpected argument"
        if self.login is not None:
            raise TypeError(message + " login")
        if self.id is not None:
            raise TypeError(message + " id")
        self.login = self.name[0] + self.surname
        self.id = generate_id()
