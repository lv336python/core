def task_555(n):
    '''
    Accepts natural number
    Return Pascal triangle
    :param n: 4
    :return:                [1]
                           [1, 1]
                         [1, 2, 1]
                        [1, 3, 3, 1]

    '''
    tringle = [[1], [1, 1]]
    for i in range(2, n):
        next_row = [1, ]

        for j in range(len(tringle[-1]) - 1):
            next_row.append(tringle[-1][j] + tringle[-1][j + 1])

        tringle.append(next_row)
        tringle[-1].append(1)
    return tringle