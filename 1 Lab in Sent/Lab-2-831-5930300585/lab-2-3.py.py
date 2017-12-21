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
