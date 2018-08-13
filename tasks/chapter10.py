""" task 332"""


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
