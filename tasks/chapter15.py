"""
This module is for tasks from chapter 15
"""
from itertools import product


def task_555(number):
    '''
    Accepts natural number
    Return Pascal triangle
    :param number: 4
    :return:                [1]
                           [1, 1]
                         [1, 2, 1]
                        [1, 3, 3, 1]

    '''
    tringle = [[1], [1, 1]]
    for _ in range(2, number):
        next_row = [1]

        for j in range(len(tringle[-1]) - 1):
            next_row.append(tringle[-1][j] + tringle[-1][j + 1])

        tringle.append(next_row)
        tringle[-1].append(1)
    return tringle


def expr(list_op):
    """Return formated string"""
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*list_op)


def gen_expr():
    """Return product for ['+', '-', ''] """
    operators = ['+', '-', '']
    return [expr(var) for var in product(operators, repeat=9) if var[0] != '+']


def task_568(val):
    """Return all possible variant for val"""
    for res_string in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())): # pylint: disable=eval-used
        print(res_string)
