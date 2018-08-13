"""
Дано натуральное число n. Получить все пифагоровы
тройки натуральных чисел, каждое из которых не превосходит n, т. е.
все такие тройки натуральных чисел a, b, c, что
a^2 + b^2 = c^2 (a ≤ b ≤ c ≤ n).
"""


def task_554(num):
    """
    Accept natural number num
    Return list of Pythagorean triplets of natural numbers each of which is lower then num
    :param num: 20
    :return: [(3, 4.0, 5.0), (4, 3.0, 5.0), (5, 12.0, 13.0), (6, 8.0, 10.0), (8, 15.0, 17.0)]
    """
    triplets_list = []
    for anum in range(3, num+1):
        if anum % 2 == 1:
            if (anum*anum+1)/2 <= num:
                triplets_list.append((anum, (anum*anum-1)/2, (anum*anum+1)/2))
        else:
            if ((anum/2)**2)+1 <= num:
                triplets_list.append((anum, ((anum/2)**2)-1, ((anum/2)**2)+1))
    return triplets_list
