def task_330(n):
    """
    Accepts natural number
    Returns True if n is perfect number and False if n is not perfect number
    :param n: 6
    :return: True
    """
    sum1 = 0
    for i in range(1, n - 1):
        if n % i == 0:
            sum1 += i
    return sum1 == n