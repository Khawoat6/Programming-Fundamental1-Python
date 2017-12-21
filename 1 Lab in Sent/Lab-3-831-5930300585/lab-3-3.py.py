def gcd(a, b):
    i = 1
    s = 0
    while (i <= a) and (i <= b):
        if (a % i) == 0 and (b % i) == 0:
            s = i
        i += 1
    return s
