##n = int(input("Enter a number: "))
##if n < 10:
##    print("The number is less than 10.")
##print("Thank you.")
##print("Good bye.")
##
##n = int(input("Enter a number: "))
##
##if n < 10 :
##    print("The number is less than 10.")
##    print("Thank you.")
##print("Good bye.")
##
##x = int(input('Enter 1st number'))
##y = int(input('Enter 2nd number'))
##
##if x < 10 or y < 10:
##    print('The number are OK.')
##print('Good bye.')
##    
##a = int(input('Enter 1st number: '))
##b = int(input('Enter 2nd number: '))
##i = 1
##while i <= a:
##    j = 1
##    while j <= i:
##        print(i,j)
##        j = j + 1
##    i = i + 1

##x=int(input('Enter 1st number:'))
##y=int(input('Enter 2nd number:'))
##if x<10 and y<10:
##    print('The numbers are OK.')
##print('Good bye.')


##age=int(input('Enter your age:'))
##if age >= 20:
##    print('You are old.')
##else:
##    print('You are young.')
##print('Good bye.')

##
##age=int(input('Enter your age:'))
##if age <= 10:
##    print('You are young.')
##else:
##    if age < 20:
##        print('You are teenager.')
##    else:
##        print('You are old.') 
##print('Good bye.')


##age=int(input('Enter your age:'))
##if age <= 10:
##    print('You are young.')
##elif age < 20:
##    print('You are teenager.')
##else:
##    print('You are old.') 
##print('Good bye.')

##n=int(input('Please enter a number:'))
##while n>0:
##    print('Too much')
##    n=int(input('Please enter a number again:'))
##print('Program terminated.')


##n=int(input('Please enter a number:'))
##while n>0:
##    print('Too much')
##print('Program terminated.')


##n=int(input('Please enter a number:'))
##while n>0:
##    print(n)
##    n=n+1
##print('Program terminated.')


##m=int(input('Enter the maximum number:'))
##d=int(input('Enter the divisor:'))
##i=1
##while i <= m:
##    if i%d == 0:
##        print(i)
##    i=i+1
##print('Program terminated.')

##a=int(input('Enter 1st number:'))
##b=int(input('Enter 2nd number:'))
##i=1
##while i <= a:
##    j = 1
##    while j <= b:
##        print(i,j)
##        j = j+1
##    i=i+1


''' **1***

print('Welcome to Change Calculator.')
price = int(input('\nPrice: '))
amount = int(input('\nAmount tendered: '))
sum = amount - price
print('\nChange: ',sum)
ot = 0                      ##One-Thousand
fh = 0                      ##Five-hundred
oh = 0                      ##One-hundred
ft = 0                      ##Fifty
tt = 0                      ##Twenty
te = 0                      ##Ten
fi = 0                      ##Five
tw = 0                      ##Two
on = 0                      ##One

ot = sum // 1000
sum = sum % 1000
if ot > 0:
    print('1000:',ot)
while sum >= 500:
    fh += 1
    sum = sum - 500
if fh > 0:
    print('500:',fh)
while sum >= 100:
    oh += 1
    sum = sum - 100
if oh > 0:
    print('100:',oh)
while sum >= 50:
    ft += 1
    sum = sum - 50
if ft > 0:
    print('50:',ft)
while sum >= 20:
    tt += 1
    sum = sum - 20
if tt > 0:
    print('20:',tt)
while sum >= 10:
    te += 1
    sum = sum - 10
if te > 0:
    print('10:',te)
while sum >= 5:
    fi += 1
    sum = sum - 5
if fi > 0:
    print('5:',fi)
while sum >= 2:
    tw += 1
    sum = sum - 2
if tw > 0:
    print('2:',tw)
if sum > 0:
    print('1:',sum)
    
print('\nThank you.')


'''

''' ***2***


pw = input('Enter the password: ')
i = 1
while (i <= 3):
    if pw == 'k7e15':
        print('The password is correct')
        i += 3
    elif(i==3):
        print('The system is disable.')
        break
    else:
        print('The password is wrong, please try again: ', end='')
        pw = input('')
        i += 1

'''



''' ***3***

import random

scnum = random.randint(1,1000000)
attempt = 0

print('Welcome to THE SECRET NUMBER')

while True:
    attempt += 1
    num = int(input('Enter a number: '))
    if num == scnum:
        break
    elif num < scnum:
        print(num ,' is too low.')
    elif num > scnum:
        print(num ,' is too high.')
print('Congratulations!!!')
print('You found the secret number in ',attempt,' times.')
        
'''


'''' ***4***

import random

scnum = random.randint(1,10)
playagain = 'y'
best = 1000000
print('Welcome to THE SECRET NUMBER')

while playagain == 'y':
    attempt = 0
    while True:
        attempt += 1
        num = int(input('Enter a number: '))
        if num == scnum:
            break
        elif num < scnum:
            print(num ,' is too low.')
        elif num > scnum:
            print(num ,' is too high.')
    print('Congratulations!!!')
    print('You found the secret number in ',attempt,' times.')
    playagain = input('Do you want to play again? (y/n): ')
    if attempt <= best:
        best = attempt

print('BEST:',best)
print('GOOD BYE.')

'''

