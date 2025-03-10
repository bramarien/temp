class calculator:
    """
    A class for basic vector operations:
    dot product, addition, and subtraction.

    Methods:
        dotproduct(V1, V2):
        Computes the dot product of two vectors.
        add_vec(V1, V2):
        Adds two vectors element-wise.
        sous_vec(V1, V2):
        Subtracts the second vector from the first element-wise.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes the dot product of two vectors.

        Args:
            V1, V2: Two vectors to compute the dot product of.

        Returns:
            None: Prints the dot product.
        """
        print(sum([x * y for x, y in zip(V1, V2)]))
        pass

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.

        Args:
            V1, V2: Two vectors to add.

        Returns:
            None: Prints the result of the addition.
        """
        print([float(x + y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first element-wise.

        Args:
            V1, V2: Two vectors to subtract.

        Returns:
            None: Prints the result of the subtraction.
        """
        print([float(x - y) for x, y in zip(V1, V2)])
