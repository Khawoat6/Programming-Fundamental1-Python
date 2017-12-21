def product_of_squares(n):
    s = 1
    for i in range(n):
        c = (n - i) ** 2
        s = s * c
        if c == 1:
            return s
