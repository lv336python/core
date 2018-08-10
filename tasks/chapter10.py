def task_329(n, m):
    """
    Accepts two natural numbers
    Returns all numbers that are smaller than n and square number of sum of digits of which are equal m
    :param n: 51
    :param m: 25
    :return: [50, 41, 32, 23, 14, 5]
    """
    sqr_root = m ** 0.5
    result = []
    for num in range(n, 0, -1):
        if sum(int(digit) for digit in str(num)) == sqr_root:
            result.append(num)
    return result