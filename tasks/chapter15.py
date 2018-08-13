""" Task 568 """
from itertools import product


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
