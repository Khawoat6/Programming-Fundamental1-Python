''''' sheet 1

EX13

n = 1573
if n > 1:
    for i in range(2, n):
        if (n % 1) == 0:
            print(n, "is not a prime number")
            print(i, "time", n//i, "is", n)
            break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


        
EX14

n = 1573
d = 2
while n > 1:
    if n % d == 0:
        n = n/d
        print(d)
    else:
        d = d+1

'''''' sheet 2

EX1
varI = input('Input Data from keyboard (Integer):')
print(varI)

varS = input('Input Data from keyboard (String):')
print(varS)

EX2
a = input('Input number; ')
sum = int(a) + 13
print(sum)

EX3
a = int(input('Input number: '))
sum = a + 13
print(sum)

EX10 (เลขสุ่มเทียม)
seed = 426
a = 293 #multiple
c = 467 #increment
m = 1000 #modulus
num = int(input("Enter a number of random number :"))
rn = seed
for i in range(1,num+1)
    rn = ((a * rn) + c) % m
    print(rn)











