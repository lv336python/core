def task_227(m, n):
    """
    Accepts two whole numbers
    Returns list of numbers that are have common divisors
    :param n: 20
    :param m: 36
    :return: [1, 2, 4]
    """
    all_div = []
    for i in range(1, min(m, n) + 1):
        if m % i == n % i == 0:
            all_div.append(i)
    return all_div
