"""
This module is for task from chapter 4
"""


def task_87(num, num_of_digits):
    """
    Accepts two natural numbers n and m
    Returns sum of the last m digits of number n
    :param num: 7242
    :param num_of_digits: 2
    :return: 8
    """
    return sum([int(digit) for digit in str(num)[-num_of_digits::]])


def task_86_b(number):
    '''
    Accepts natural number.
    Returns sum of number digits.
    :param number: 354
    :return:  12
    '''
    return sum([int(i) for i in list(str(number))])


def task_108(number):
    '''

    Accepts natural number.
    Return the first number like 2^r which is greater than our number
    :param number:   3   |   453
    :return:    4   |   512
    '''
    power = 0
    while True:
        if 2 ** power > number:
            break
        else:
            power += 1
    return 2 ** power


def task_88_h(number):
    """ Return int"""
    number = str(number)
    if not number.isdigit():
        return 'Enter a valid number'
    return int('1' + number + '1')


def task_86g(num, sign=1):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(num, int):
        the_sum = 0
        num = int(str(num)[::-1])  #reverse of number
        while num:
            the_sum += num%10 * sign  #n%10 - last digit in number
            # print('n%10 * sign=> ', n%10 * sign)
            # print('sum=> ',sum)
            num = num // 10
            sign *= -1
    else:
        return 'You need to enter THE integer'
    return the_sum


def task_86g_1(num):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(num, int):
        num = list(str(num)) #convert int to list with strs
        my_list = [] #just to show  how mutable type works
        my_list = [my_list.append(int(i)) for i in num]#update List to each elem int
        index = 1
        the_sum = 0
        while my_list:
            try:
                my_list[index] *= -1
                index += 2
            except IndexError: #avoid index error
                break #stop loop
        for i in my_list:
            the_sum += i
    else:
        return 'You need to enter THE integer'
    return the_sum
