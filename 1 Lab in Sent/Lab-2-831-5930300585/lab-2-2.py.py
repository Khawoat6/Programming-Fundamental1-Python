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
pw = input("Enter the password : ")
x = 1
while ( x < 3 ):
    if ( pw == "k7e15"):
        print("The password is correct.")
    else:
        pw = input("The password is wrong, please try again: ")
        x = x+1
