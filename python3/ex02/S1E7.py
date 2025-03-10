from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a formal string for debugging."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="blue", hairs="light"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a formal string for debugging."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_lannister(first_name: str | list, is_alive=True):
        """
        Create one or more Lannister characters.

        Args:
            first_name (str or list):
            A single name or a list of names.
            is_alive (bool):
            Whether the characters are alive. Defaults to True.

        Returns:
            Lannister or list: A single Lannister or a list of Lannisters.
        """
        if isinstance(first_name, list):
            return [Lannister(item, is_alive) for item in first_name]
        else:
            return Lannister(first_name, is_alive)
