a = []
b = []
def multiply(x, y):
    z =[[0 for row in range(len(x))] for col in range(len(y[0]))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                c[i][j] += a[i][k]*b[k][j]
    return z
