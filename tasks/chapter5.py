def task_224(num):
    """
    Accept natural number num
    Return all natural dividers of num
    :param num: 25
    :return: 3
    """

    count = len([x for x in range(1, num + 1) if num % x == 0])
    return count
