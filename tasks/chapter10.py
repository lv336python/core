"""
This module for tasks from chapter 10
"""


def task_325(number):
    '''
    Accepts natural number
    Return all simple numbers which is dividers of natural number n
    :param number: 100       | 652
    :return: [1, 2, 5]  | [1, 2, 163]
    '''
    result = [1, ]
    for i in range(2, number):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            if number % i == 0:
                result.append(i)

    return result


def task_332(digit):
    """
    Return list of number or None

    :param digit: int
    :return list or None:
    """

    max_number = round((digit ** (1 / 2)) + 0.5)
    for x_val in range(max_number):
        for y_val in range(max_number):
            for z_val in range(max_number):
                for t_val in range(max_number):
                    if x_val ** 2 + y_val ** 2 + z_val ** 2 + t_val ** 2 == digit:
                        return [x_val, y_val, z_val, t_val]
    return None
