"""
    Accepts natural numbers
    Returns pairs of amicable numbers
    :param n_values: 200
    :param m_values: 300
    :return: [(257, 263), (257, 269), (257, 271), (257, 277), (257, 281), ...
"""


def task_560(n_v, m_v):
    """Returns pairs of amicable numbers"""
    result = []
    d_n = {num: [x for x in range(1, int(num / 2) + 1) if num % x == 0] for num in range(n_v, m_v)}
    for i in d_n.keys():
        for j in d_n.keys():
            if sum(d_n[i]) == sum(d_n[j]) and i != j:
                result.append((i, j))
    return result

