a = input('Enter the password: ')
b = "k"
i=0
while(i<3):
  if(a==b):
    print('The password is correct.')
    break
  elif(a!=b and i>=2):
    print('The system is disable.')
    break
  a=input(('The password is wrong, please try again:'))
  i+=1

    
