#8A_solution

'''def sum_money(data):
    value = (1,5,10,50,100,500,1000)
    sum_money = 0
    for i in range(7):
        sum_money += (data[i]*value[i])
        return sum_money
'''

'''n = ()
def sum_money(n):
    a = n[0]*1
    b = n[1]*5
    c = n[2]*10
    d = n[3]*50
    e = n[4]*100
    f = n[5]*500
    g = n[6]*1000
    return a+b+c+d+e+f+g
'''

'''
def calculate_balance(data):
    sum_money = 0
    for i in range(len(data)):
        if data[i][0] == 'D':
            sum_money += data[i][1]
        else:
            if sum_money > data[i][1]:
                sum_money -= data[i][1]
    return sum_money
'''

'''m = []
def calculate_balance(m):
    s = 0
    for i in range(len(m)):
        if m[i][0] == 'D':
            s = s+m[i][1]
        else:
            if s >m[i][1]:
                s = s-m[i][1]
    return s
'''

'''
def is_triangular_number(data):
    n = 0
    while (True):
        if (n*(n+1))/2 == data:
            return True
        elif(n*(n+1))/2 > data:
            return False
        else:
            n += 1
'''

'''def is_triangular_number(n):
    for i in range(n):
         if i*(i+1)/2 == n:
            return True
    return False
'''



#8B_solution
'''
def pass_birthday_rule(data):
    date_set = (15,6,2530)
    for i in range(2,-1,-1):
        if date_set[i] < data[i]:
            return True
        elif date_set[i] > data[i]:
            return False
        else:
            continue
'''

'''p = ()
def pass_birthday_rule(p):
    d = p[0]
    m = p[1]
    y = p[2]
    d1 = 15
    m1 = 6
    y1 = 2530

    if y > y1:
        return True
    if y < y1:
        return False
    if y == y1:
        if m >= m1:
            if d >= d1:
                return True
    if y == y1:
        if m < m1:
            return False
    if y == y1:
        if m == m1:
            if d < d1:
                return False
'''

'''
def sum_money(data):
    money_type = [1,2,5,10,20,50,100,500,1000]
    sum_money = 0
    for i in range(len(data)):
        if (data[i][0] in money_type):
            sum_money += (data[i][0] * data[i][1])
        return (sum_money)
'''

'''def sum_money(m):
    f = 0
    for i in range(len(m)):
        if m[i][0] == 1  :
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 2:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 5:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 10:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 20:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 50:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 100:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 500:
            f = f+m[i][0]*m[i][1]
        if m[i][0] == 1000:
            f = f+m[i][0]*m[i][1]
    return f
'''
        
'''
def prime(d):
    prime_ls = [2,3]
    if d < 3:
        return prime_ls[d-1]
    n =2
    while(n != d):
        new_p = prime_ls[-1]+2 
        pointer = 0
        while pointer != len(prime_ls):  
            if new_p % prime_ls[pointer] == 0: 
                new_p += 2
                pointer = 0
            else:
                pointer += 1
        prime_ls.append(new_p)
        n += 1
    return prime_ls[d-1]
'''




