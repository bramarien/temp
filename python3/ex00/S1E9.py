from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class for a character.
    Attributes:
        first_name (str): The character's first name.
        is_alive (bool): Whether the character is alive. Default is True.
    Methods:
        die(): Marks the character as dead. Must be implemented by subclasses.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes the character with a name and alive status.
        Args:
            first_name (str): The character's first name.
            is_alive (bool): Whether the character is alive (default is True).
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Marks the character as dead. To be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Represents a Stark character.
    Methods:
        die(): Marks the Stark character as dead.
    """

    def die(self):
        """Marks the Stark character as dead by setting is_alive to False."""
        self.is_alive = False
