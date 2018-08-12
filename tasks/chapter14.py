def task_554(n):
    """
    Accept natural number n
    Return list of Pythagorean triplets of natural numbers each of which is lower then n
    :param n: 20
    :return: [(3, 4.0, 5.0), (4, 3.0, 5.0), (5, 12.0, 13.0), (6, 8.0, 10.0), (8, 15.0, 17.0)]
    """

    triplets_list = []
    for a in range(3, n+1):
        if a % 2 == 1:
            if (a*a+1)/2 <= n:
                triplets_list.append((a, (a*a-1)/2, (a*a+1)/2))
        else:
            if ((a/2)**2)+1 <=n:
                triplets_list.append((a, ((a/2)**2)-1, ((a/2)**2)+1))
    return triplets_list