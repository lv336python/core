"""
Task 225
"""
def task_225(number):
    '''
    Accepts natural number
    Return all number from range <i = 1 to n >, if n % i*i == 0  and n % i*i*i != 0
    :param number: 54531 |   123456
    :return:  [3,]  |   [8,]
    '''
    return [i for i in range(1, number) if number % i ** 2 == 0 and number % i ** 3 != 0]
