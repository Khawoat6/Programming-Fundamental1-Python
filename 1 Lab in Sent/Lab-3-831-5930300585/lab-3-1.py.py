def is_perfect_number(n):
    i = 1
    s = 0
    if type(n) == int:
        while i < n:
            if (n % i) == 0:
                s += i
            i += 1
    if n == s:
        return True
    else:
        return False


'''
def is_perfect_number(n):
    #Return True if n is a perfect number.
    #Otherwise, return False.
    x = 0
    y = 2
    if type(n) == int or type(n) ==float:
        #A perfect number must be an integer
        #Or a perfect number must be an flating-point
        while y <= n:
            a = n
            b = a/y
            if a % y == 0:
                x = x + b
            y += 1
        if x == n:
            return True
        if x != n:
            return False
    else:
        return False
