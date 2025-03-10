class calculator:
    """
    A class that performs element-wise operations (addition, subtraction,
    multiplication, division) on a vector with a scalar.
    """

    def __init__(self, vector: list):
        """
        Initializes the calculator with a vector.

        Parameters:
            vector (list): A list of numeric values representing the vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adds a scalar to each element of the vector and prints the result.

        Parameters:
            object (int or float): The scalar to add to each element.
        """
        self.vector = [item + object for item in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplies each element of the vector by a scalar
        and prints the result.

        Parameters:
            object (int or float): The scalar to multiply with each element.
        """
        self.vector = [item * object for item in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtracts a scalar from each element of the vector
        and prints the result.

        Parameters:
            object (int or float): The scalar to subtract from each element.
        """
        self.vector = [item - object for item in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divides each element of the vector by a scalar
        and prints the result.

        Parameters:
            object (int or float): The scalar to divide each element by.

        Raises:
            ValueError: If the scalar is 0.
        """
        if object == 0:
            raise ValueError("Division by 0 is not allowed")
        self.vector = [item / object for item in self.vector]
        print(self.vector)
