import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15-character string consisting
    of lowercase ASCII letters.

    Returns:
        A 15-character string with random lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student with a name, surname, and other attributes.

    Attributes:
        name: The first name of the student.
        surname: The surname of the student.
        active: A boolean indicating if the student is active
        (default is True).
        login: A string representing the student's login,
        derived from their name and surname.
        id: A unique identifier for the student, generated automatically.

    Methods:
        __post_init__: Sets the student's login
        based on their name and surname.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Post-initialization method to generate the student's login.

        This method sets the student's login by concatenating
        the first letter of their surname
        with the first 7 characters of their first name.
        """
        self.login = self.surname[0] + self.name[:7]
