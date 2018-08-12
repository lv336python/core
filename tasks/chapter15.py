def task_560(n, m):
    """
    Accepts natural numbers
    Returns pairs of amicable numbers
    :param n: 200
    :param m: 300
    :return: (220, 284)
    """
    tup1 = (0, 0)
    for i in range(n, m):
        proper_div1 = sum_divs(i)
        if n <= proper_div1 <= m:
            proper_div2 = sum_divs(proper_div1)
            if proper_div2 == i:
                tup1 = (proper_div2, proper_div1)
                return tup1
    return tup1


def sum_divs(num):
    sum1 = 0
    for i in range(num):
        if i > 0:
            if num % i == 0:
                sum1 = sum1 + i
    return sum1
