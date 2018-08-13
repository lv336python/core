# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 569
Дано натуральное число number. Получить в порядке возрастания
n первых натуральных чисел, которые не делятся ни на какие простые
числа, кроме 2, 3 и 5. 2 Variants.
"""

def task_569(num):
    """
    Given a natural number n.
    Return sequence of numbers that % (2,3,5) == 0
    """
    count = 0
    k = 1
    result = ''
    while count != num:
        if k % 2 == 0 or k % 3 == 0 or k % 5 == 0:
            result = result + ' ' + str(k)
            count += 1
        k += 1
    return result


def task_569_check(num):
    """
    Given a natural number n.
    Return sequence of numbers that % (2,3,5) == 0
    """
    sequence_list = []
    for i in range(1, num + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            sequence_list.append(i)
            sequence_tuple = tuple(sequence_list)#sequence in one row
    return sequence_tuple
