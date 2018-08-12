def task_225(n):
    '''
    Accepts natural number
    Return all number from range <i = 1 to n >, if n % i*i == 0  and n % i*i*i != 0
    :param n: 54531 |   123456
    :return:  [3,]  |   [8,]
    '''
    return [i for i in range(1, n) if n % i ** 2 == 0 and n % i ** 3 != 0]


