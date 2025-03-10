from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a King, inheriting from Baratheon and Lannister.

    Methods:
        set_eyes(color): Sets the eye color of the King.
        set_hairs(color): Sets the hair color of the King.
        get_eyes(): Returns the eye color of the King.
        get_hairs(): Returns the hair color of the King.
    """

    def set_eyes(self, color: str):
        """
        Sets the eye color.

        Args:
            color (str): The color of the eyes.
        """
        self.eyes = color

    def set_hairs(self, color: str):
        """
        Sets the hair color.

        Args:
            color (str): The color of the hair.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Returns the eye color.

        Returns:
            str: The color of the eyes.
        """
        return (self.eyes)

    def get_hairs(self):
        """
        Returns the hair color.

        Returns:
            str: The color of the hair.
        """
        return (self.hairs)
