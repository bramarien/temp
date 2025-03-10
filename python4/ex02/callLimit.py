def callLimit(limit: int):
    """
    Returns a decorator that limits the number of times a function
    can be called.

    Args:
        limit: The maximum number of times
        the decorated function can be called.

    Returns:
        A decorator function (`callLimiter`) that enforces the limit
        on the number of calls.
    """
    count = limit

    def callLimiter(function):
        """
        A decorator that limits the number of calls to the decorated function.

        Args:
            function: The function to be decorated.

        Returns:
            A new function (`limit_function`) that enforces the call limit.
        """
        def limit_function(*args: any, **kwds: any):
            """
            A function that checks if the call limit has been exceeded
            and either
            calls the original function or prints an error message.

            Args:
                *args: Positional arguments to pass to the original function.
                **kwds: Keyword arguments to pass to the original function.

            Returns:
                The result of the original function
                if the call limit hasn't been exceeded.
                Otherwise, it prints an error message.
            """
            nonlocal count
            count -= 1
            if (count < 0):
                print(f"{function} call too many times")
                return
            return function(*args, **kwds)
        return limit_function
    return callLimiter
