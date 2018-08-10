
def task_178b(numbers):
    """
    Accepts list of natural numbers
    Returns amount of numbers that are divisible by 3 and not divisible by 5.
    :param nums: [1, 52, 12, 25, 5, 2, 3]
    :return: 2
    """
    quantity = 0
    for num in numbers:
        if num % 3 == 0 and num % 5 != 0:
            quantity += 1
    return quantity


def task_226(n, m):
    """
    Accepts two natural numbers
    Returns list of numbers that are divisible by both n and m and are less or equal m*n
    :param n: 12
    :param m: 3
    :return: [36, 24, 12]
    """
    bigger = max(n, m)
    smaller = min(n, m)
    return [num for num in range(m*n, bigger-1, -bigger) if num % smaller == 0]
