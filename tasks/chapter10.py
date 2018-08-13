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


def task_340(number, *args):
    """
    Given number and sequence
    Return a i + a j + a k = m or info abt error
    """
    assert number <= 60 and len(args) == 20
    args = list(args)
    print(args)
    for i in args:
        for j in args:
            for k in args:
                if i + j + k == number:
                    return 'Found: ' \
                           '{},  {} + {} + {} = {}'.format((i, j, k), i, j, k, number)
    return  'Not found any ' \
            'match accordint to the patter ' \
            'args[i] + args[j] + args[k] == {}'.format(number)


def task_329(num_1, num_2):
    """
    Accepts two natural numbers
    Returns all numbers that are smaller than n and square
    number of sum of digits of which are equal m
    :param num_1: 51
    :param num_2: 25
    :return: [50, 41, 32, 23, 14, 5]
    """
    sqr_root = num_2 ** 0.5
    result = []
    for num in range(num_1, 0, -1):
        if sum(int(digit) for digit in str(num)) == sqr_root:
            result.append(num)
    return result


def task_331_b(num):
    '''
    Function finds all triplets of x,y,z for which x^2 + y^2 + z^2= num.
    Return will be a list of tuples with x,y,z with all possible combinations.
    '''
    max_n = int(num**0.5)+1 # will limit range and reduce check time
    triplets = []
    for x_n in range(1, max_n):
        for y_n in range(1, max_n):
            for z_n in range(1, max_n):
                if x_n**2 + y_n**2 + z_n**2 == num:
                    triplet = (x_n, y_n, z_n)
                    triplets.append(triplet)
    return triplets


def task_323(num):
    """
    Accept natural number num
    Return mutually simple numbers with num and lower then num
    :param num: 20
    :return: [1, 3, 7, 9, 11, 13, 17, 19]
    """
    msp_list = []
    for anum in range(1, num):
        buf = anum
        bnum = num

        while bnum != 0 and anum != 0:
            if bnum > anum:
                bnum = bnum % anum
            else:
                anum = anum % bnum

        if bnum+anum == 1:
            msp_list.append(buf)
    return msp_list

