"""
Дано натуральное число n. Получить все натуральные
числа, меньшие n и взаимно простые с ним.
"""


def task_323(num):
    """
    Accept natural number num
    Return mutually simple numbers with num and lower then num
    :param num: 20
    :return: [1, 3, 7, 9, 11, 13, 17, 19]
    """
    msp_list = []
    for anum in range(1, num):
        buf = anum
        bnum = num

        while bnum != 0 and anum != 0:
            if bnum > anum:
                bnum = bnum % anum
            else:
                anum = anum % bnum

        if bnum+anum == 1:
            msp_list.append(buf)
    return msp_list
