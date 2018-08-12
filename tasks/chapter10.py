def task_323(n):
    """
    Accept natural number n
    Return mutually simple numbers with n and lower then n
    :param n: 20
    :return: [1, 3, 7, 9, 11, 13, 17, 19]
    """

    msp_list = []
    for a in range(1, n):
        buf = a
        b = n

        while b != 0 and a != 0:
            if b > a:
                b = b % a
            else:
                a = a % b

        if b+a == 1:
            msp_list.append(buf)
    return msp_list