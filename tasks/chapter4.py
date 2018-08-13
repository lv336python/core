'''Tasks for chapter 4'''

def  task_88_c(num):
    '''
    Function swap last and first digit of given number.
    Input have to be an integer.
    Example: 3*****5 >> 5*****3
    '''
    iter_num = list(str(num)) #making number iterable
    iter_num[0], iter_num[-1] = iter_num[-1], iter_num[0] #swapping digits
    return int(''.join(iter_num)) #output type is the same as input
