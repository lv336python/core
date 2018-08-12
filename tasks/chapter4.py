# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 86(g)
Дано натуральное число n. Найти знакочередующуюся сумму цифр числа n (пусть запись n в десятичной системе есть α k α k − 1 ... α 0 ;
найти α k − α k − 1 + ... + ( − 1 ) k α 0 ). 2 Variants.
"""

def task_86g(n, sign=1):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(n, int):
        sum = 0
        n = int(str(n)[::-1])  #reverse of number
        while n:
            sum += n%10 * sign  #n%10 - last digit in number
            # print('n%10 * sign=> ', n%10 * sign)
            # print('sum=> ',sum)
            n = n // 10
            sign *= -1
    else:
        return 'You need to enter THE integer'
    return sum


def task_86g_1(n):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(n, int):
        n = list(str(n)) #convert int to list with strs
        List = [] #just to show  how mutable type works
        [List.append(int(i)) for i in n]#update List to each elem int
        index = 1
        sum = 0
        while List:
            try:
                List[index] *= -1
                index += 2
            except IndexError: #avoid index error
                break #stop loop
        for i in List:
            sum += i
    else:
        return 'You need to enter THE integer'
    return sum

