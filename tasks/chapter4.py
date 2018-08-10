

def task_87(n, m):
    if n < 0:
        return None
    elif m <= 0:
        return None
    elif m > len(str(n)):
        return None
    return sum([int(i) for i in str(int(n))[-m::]])

