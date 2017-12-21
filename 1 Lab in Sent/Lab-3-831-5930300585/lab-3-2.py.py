def factorial(n):
    i = 1
    s = 1
    if n >= 0:
        if n == 0:
            return 1
        else:
            while i <= n:
                s = s * i
                i += 1
            return s
    else:
        return None
