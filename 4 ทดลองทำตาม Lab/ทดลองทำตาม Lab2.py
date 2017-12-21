####Interjective Control Lab2

##n = int(input("Enter your name:"))
##if n < 10:
##    print("The number is less than 10.")
##print("Thank you.")
##print("Good bye.")

##n = int(input("Enter your name:"))
##if n < 10:
##    print("The number is less than 10.")
##    print("Thank you.")
##print("Good bye.")

##x = int(input('Enter 1st number:'))
##y = int(input('Enter 2nd number:'))
##if x<10 or y<10:
##    print('The numbers are OK.')
##print('Good bye.')

##x = int(input('Enter 1st number:'))
##y = int(input('Enter 2nd number:'))
##if x<10 and y<10:
##    print('The numbers are OK.')
##print('Good bye.')

##age = int(input('Enter your age:'))
##if age >= 20:
##    print('You are old.')
##print('Good bye.')
          
##age = int(input('Enter your age:'))
##if age >= 20:
##    print('You are old.')
##else:
##    print('You are young.')
##print('Good bye.')

##age = int(input('Enter your age:'))
##if age <= 10:
##    print('You are young.')
##else:
##    if age < 20:
##        print('You are a teenager.')
##    else:
##        print('You are old.')
##print('Good bye.')

##age = int(input('Enter your age:'))
##if age <= 10:
##    print('You are young.')
##elif age < 20:
##    print('You are a teenager.')
##else:
##    print('You are old.')
##print('Good bye.')

####while
##n = int(input('Please enter a number:'))
##while n > 0:
##    print('Too much.')
##    n = int(input('Please enter a number again:'))
##print('Program terminated.')

##n = int(input('Please enter a number:'))
##while n > 0:
##    print('Too much.')
##print('Program terminated.')

##n = int(input('Please enter a number:'))
##while n > 0:
##    print(n)
##    n = n - 1
##print('Program terminated.')

##n = int(input('Please enter a number:'))
##while n > 0:
##    print(n)
##    n = n + 1
##print('Program terminated.')

##m = int(input('Enter the maximum number:'))
##d = int(input('Enter the divisor:'))
##i = 1
##while i <= m:
##    if i%d == 0:
##        print(i)
##    i = i + 1
##print('Program terminated.')
#### m = stop , d = start

##a = int(input('Enter 1st number:'))
##b = int(input('Enter 2nd number:'))
##i = 1
##while i <= a:
##    j = 1
##    while j <= b:
##        print(i,j)
##        j = j + 1
##    i = i + 1

##a = int(input('Enter 1st number:'))
##b = int(input('Enter 2nd number:'))
##i = 1
##while i <= a:
##    j = 1
##    while j <= i:
##        print(i,j)
##        j = j + 1
##    i = i + 1




'''Excample'''

''' ***1***


print("Welcome to Change Calculator.\n")
pr = int(input("Price: "))
am = int(input("\nAmount tendered: "))
ch = am-pr
print("\nChange: ",ch)
yq = 0                #yiqian
wb = 0                #wubai
yb = 0                #yibai
ws = 0                #wushi
s  = 0                #shi
w  = 0                #wu
e  = 0                #er
y  = 0                #yi
while(ch >= 1000):
    yq = yq + 1
    ch = ch - 1000
while(ch >= 500):
    wb = wb + 1
    ch = ch - 500
while(ch >= 100):
    yb = yb + 1
    ch = ch - 100
while(ch >= 50):
    ws = ws + 1
    ch = ch - 50
while(ch >= 20):
    s = s + 1
    ch = ch - 20
while(ch >= 10):
    w = w + 1
    ch = ch - 10
while(ch >= 5):
    e = e + 1
    ch = ch - 5
while(ch >= 2):
    y = y + 1
    ch = ch - 2
if(yq > 0):
    print("1000: ",yq)
if(wb > 0):
    print("500: ",wb)
if(yb > 0):
    print("100: ",yb)
if(ws > 0):
    print("50: ",ws)
if(s > 0):
    print("20: ",s)
if(w > 0):
    print("10: ",w)
if(e > 0):
    print("5: ",e)
if(y > 0):
    print("2: ",y)
if(ch > 0):
    print("1 ",ch)
print("\nThank you.")

'''



''' ***2***


baima = input("Enter the password: ")
#baima = password
x = 1
while( x <= 3):
    if(baima == "k7e15"):
        print("The password is correct.")
        x = x+3
    elif(x==3):
        print("The system is disable.")
        x = x+1
    else:
        baima = input("The password is wrong, please try again: ")
        x = x+1

'''



''' ***3***


import random

scnum = random.randint(1,1000000)
attempt = 0

print("Welcome to THE SECRET NUMBER")

while True:
    attempt += 1
    num = int(input("Enter a number:"))
    if num == scnum:
        break
    elif num < scnum:
        print(num ,"is too low.")
    elif num > scnum:
        print(num ,"is too high.")
print("Congratulation!!!")
print("You found the secret number in",attempt,'times.')

'''



''' ***4***


import random

scnum = random.randint(1,1000000)
playagain = "y"
best = 1000000
print("Welcome to THE SECRET NUMBER")

while playagain == "y":
    attempt = 0
    while True:
        attempt += 1
        num = int(input("Enter a number: "))
        if num == scnum:
            break
        elif num < scnum:
            print(num,"is too low.")
        elif num > scnum:
            print (num,"is too high.")
    print("Congratulations!!!")
    print("You found the secret number in ",attempt," times.")
    playagain = input("Do you want to play again? (y/n): ")
    if attempt <= best:
        best = attempt

print("BEST:",best)
print("GOOD BYE.")

'''

    
