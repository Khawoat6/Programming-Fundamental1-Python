#### Function

### 3.1 Basic Function

##def free():
##    print("I am free!!!")

##def free():
##    print("I am free!!!")
##print(type(free))
##print(free)

##def free():
##    print("I am free!!!")
##print(type(free))
##free()

##def free():
##    i = 0
##    while i < 3:
##        print("I am free!!!")
##    i += 1
##print(type(free))
##free()

#### 3.2 [square,return]
##def square(x):
##    print(x**2)
##square(5)

### print(x**2)
##square(-30)       900
##square(24.69)     609.5961000000001
##square(6-2)       16
##square("FREE")    Error

##def square(x):
##    return x**2
##square(5)

##def square(x):
##    return x**2
##print(square(5))

##def square(x):
##    return x**2
##s = square(5)
##print(s)

### change s = square(5)
##s = 3 + square(-30)               903
##s = square(24.69)/7               87.08515714285716
##s = square(6-2) + square(-3)      25
##s = square(square(4)+5.37)        87.7969000000...
##s = "FREE" * square(-2)           FREE FREE FREE FREE

##def range_sum(a,b):
##    s = 0
##    i = a
##    while i <= b:
##        s += i
##        i += 1
##    return s

##                    def age_check(name,age):
##                        print('Hey',name,age = '')
##                        if age >= 40:
##                            print(',you are old.')
##                        else:
##                            print(',you are young.')

### 3.3 [None , default parameter]











