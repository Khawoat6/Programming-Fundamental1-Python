##def is_prime(n):
##    # Return True if n is a prime number
##    # otherwise, retuen False
##
##    if type(n) != int:
##        return False # A prime must be an integer
##    elif n <= 1:
##        return False # A prime must be more than 1.
##    else:
##        # For n more than 1,
##        # check that if there is an int i(1<i<n) such that n%1==0
##        # If ther is such i, n is not prime.
##
##        i = 2
##        while i<n:
##            if n%i ==0:
##                return False
##            i += 1
##        return True
##
##def generate_primes(to, start_at = 1):
##    # Print all prime numbers in the range[start_at,to]
##
##    i = start_at
##    while i <= to:
##        if is_prime(i):
##            print(i)
##        i += 1
##
##
##def f1(a):
##    b = 10
##    print("IN f1, a = "+str(a)+", b = "+str(b))
##    
##a = 1
##b = 2
##print("In global, a = "+str(a)+",b = "+str(b))
##f1(a+b)
##print("In global, a = "+str(a)+",b = "+str(b))
##
##def f1(a):
##    print("In f1, a = "+str(a)+", b = "+str(b))
##a = 1
##b = 2
##f1(a+b)
##
##def r1(n):
##    if n>0:
##        print(n)
##        r1(n+1)
##def p(a,b):
##    if b == 0:
##        return 1
##    else:
##        return a * p(a, b-1)
##
##def d12(n):
##    print("fib(",n,")")
##    if n <= 1:
##          return n
##    else:
##          return d12(n-1) + d12(n-2)



    
''' ***1***


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
 

''' ***2***


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

'''

''' ***3***

def gcd(a, b):
    i = 1
    s = 0
    while (i <= a) and (i <= b):
        if (a % i) == 0 and (b % i) == 0:
            s = i
        i += 1
    return s

'''

''' ***4***


def range_product(to, start_at = 1):
    if to > start_at:
        return to * range_product(to-1, start_at)
    elif to == start_at:
        return 1 * to
    else:
        return None

'''
    
    
    

    
    
        
        

            
