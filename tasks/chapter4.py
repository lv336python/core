

def task_87(n, m):
    """
    Accepts two natural numbers n and m
    Returns sum of the last m digits of number n
    :param n: 7242
    :param m: 2
    :return: 8
    """
    if not isinstance(n, int):
        raise TypeError(f"n must be int, not {type(n).__name__}")
    elif not isinstance(m, int):
        raise TypeError(f"m must be int, not {type(m).__name__}")
    elif n < 1 or m < 1:
        raise ValueError("must be a natural number (bigger than 0)")
    elif m > len(str(n)):
        raise ValueError("m must be smaller than number of n's digits")

    return sum([int(i) for i in str(n)[-m::]])
