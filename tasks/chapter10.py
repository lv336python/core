# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 340
Даны целые числа number, a 1 , .... ,a 20 . Найти три натуральных числа i, j, k ,
каждое из которых не превосходит двадцати, такие, что
a i + a j + a k = m . Если таких чисел нет, то сообщить об этом.
"""

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
