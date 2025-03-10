def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Computes and prints statistical measures
    (mean, median, quartiles, std, var) for the given numeric arguments.

    Args:
        *args: A list of numerical values (int or float)
        for statistical calculations.
        **kwargs: Key-value pairs where the key is a statistical measure
        ('mean', 'median', 'quartile', 'std', 'var').

    Prints the result for the requested measure(s).
    """
    for index, value in kwargs.items():
        if all(isinstance(arg, int | float) for arg in args) and args:
            match value:
                case "mean":
                    res = sum(args) / len(args)
                case "median":
                    res = list(args)
                    med_pos = len(res) // 2
                    res.sort()
                    res = res[med_pos]
                case "quartile":
                    max = len(args)
                    res = list(args)
                    res.sort()
                    res = [res[int(max*0.25)], res[int(max*0.75)]]
                case "std":
                    mean = sum(args) / len(args)
                    res = (sum([(arg - mean)**2 for arg in args]) / len(args))
                    res = res ** 0.5
                case "var":
                    mean = sum(args) / len(args)
                    res = sum([(arg - mean)**2 for arg in args]) / len(args)
                case _:
                    continue
            print(f"{value}: {res}")
        else:
            print("ERROR")
