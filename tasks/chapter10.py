def task_325(n):
    '''
    Accepts natural number
    Return all simple numbers which is dividers of natural number n
    :param n: 100       | 652
    :return: [1, 2, 5]  | [1, 2, 163]
    '''
    result = [1, ]
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            if n % i == 0:
                result.append(i)

    return result


