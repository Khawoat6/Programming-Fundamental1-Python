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
