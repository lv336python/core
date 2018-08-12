# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 340
Даны целые числа m, a 1 , .... ,a 20 . Найти три натуральных числа i, j, k , каждое из которых не превосходит двадцати, такие, что
a i + a j + a k = m . Если таких чисел нет, то сообщить об этом.
"""

def task_340(m, *args):
    assert m <= 60 and len(args) == 20
    args = list(args)
    print(args)
    for i in range(len(args)):
        for j in range(len(args)):
            for k in range(len(args)):
                if args[i] + args[j] + args[k] == m:
                    return 'Found: {},  {} + {} + {} = {}'.format((args[i],
                                                                   args[j], args[k]), args[i], args[j], args[k], m)
    return  'Not found any match accordint to the patter args[i] + args[j] + args[k] == {}'.format(m)


