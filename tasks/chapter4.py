# by Volodymyr Petryna, Python 3.6.6

"""
Exercise 86(g)
Дано натуральное число num. Найти знакочередующуюся сумму цифр числа n
(пусть запись n в десятичной системе есть α k α k − 1 ... α 0 ;
найти α k − α k − 1 + ... + ( − 1 ) k α 0 ). 2 Variants.
"""

def task_86g(num, sign=1):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(num, int):
        the_sum = 0
        num = int(str(num)[::-1])  #reverse of number
        while num:
            the_sum += num%10 * sign  #n%10 - last digit in number
            # print('n%10 * sign=> ', n%10 * sign)
            # print('sum=> ',sum)
            num = num // 10
            sign *= -1
    else:
        return 'You need to enter THE integer'
    return the_sum


def task_86g_1(num):
    """
    Given n(number).
    Return α k − α k − 1 + ... + ( − 1 ) k α 0 )
    """
    if isinstance(num, int):
        num = list(str(num)) #convert int to list with strs
        my_list = [] #just to show  how mutable type works
        my_list = [my_list.append(int(i)) for i in num]#update List to each elem int
        index = 1
        the_sum = 0
        while my_list:
            try:
                my_list[index] *= -1
                index += 2
            except IndexError: #avoid index error
                break #stop loop
        for i in my_list:
            the_sum += i
    else:
        return 'You need to enter THE integer'
    return the_sum
