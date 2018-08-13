"""
    This module is for task from Chapter 7
"""
import math


def task_178_v(*n):
    """Returns number of sequence members"""
    count = 0
    for i in n:
        if math.sqrt(i) % 2 == 0:
            count += 1
    return count


def task_227(m_values, n_values):
    """Returns list of numbers that are have common divisors"""
    all_div = []
    for i in range(1, min(m_values, n_values) + 1):
        if m_values % i == n_values % i == 0:
            all_div.append(i)
    return all_div
