

def task_87(n, m):
    if n < 0:
        return None
    elif m <= 0:
        return None
    elif m > len(str(n)):
        return None
    return sum([int(i) for i in str(int(n))[-m::]])


if __name__ == '__main__':
    print(task_87(32636, 3))
    print(task_87(32636, 5))
    print(task_87(32636, 0))
    print(task_87(32636, 85))

