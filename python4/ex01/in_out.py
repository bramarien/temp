def square(x: int | float) -> int | float:
    """
    Returns the square of the given number.

    Args:
        x: A numerical value (int or float).

    Returns:
        The square of the input number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns the result of raising the number to the power of itself.

    Args:
        x: A numerical value (int or float).

    Returns:
        The number raised to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a closure that applies the given function
    to the input number iteratively.

    Args:
        x: A numerical value (int or float).
        function: A function that takes a numerical value
        and returns a numerical value.

    Returns:
        A function that, when called, applies the given function to `x`
        and returns the result.
    """
    count = x

    def inner() -> float:
        """
        A closure function that applies the provided function
        to the current value of `count` and returns the updated result.

        The function modifies `count` using the `nonlocal` keyword to reflect
        the changes made within the `outer` function.

        Returns:
            The updated value of `count` after applying the function.
        """
        nonlocal count
        count = function(count)
        return count

    return inner
