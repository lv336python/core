
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
