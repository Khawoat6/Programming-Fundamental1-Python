def binary_string(z):
    if z == 0:
        return '0'
    if z > 0:
        return ("{0:b}".format(z))

'''
def binary_sting(x):
    a = 2
    i = ''
    if x < 0:
        return None
    if x == 0:
        return '0'
    while x > 0:
        y = x % a
        x = x // a
        if y == 0:
            i = '0' + i
        elif y == 1:
            i = '1' + i
    return i
'''

'''
def binary_sting(n):
    result = ''
    if n == 0:
        result = '0'
    while n >= 1:
        if (n % 2) == 1:
            result = '1' + result
        else:
            result = '0' + result
        n = n // 2
    return result
'''
