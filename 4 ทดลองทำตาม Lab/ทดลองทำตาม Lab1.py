###Start Python Lab1

##print('I love \'Python\'.')       =   I love 'Python'. 
##print("I love \'Python\'.")       =   I love 'Python'.
##print("I love 'Python'.")         =   I love 'Python'.
##print("I love \"Python\".")       =   I love "Python".
##print("I love \\\"Python\\\".")   =   I love \"Python\".

##print("\"Logic will get you from \'A\' to \'B\'")
##print("Imagination will take you everywhere\".")
##print("-- Albert Einstein")

##print('Ha' + 'wai')          =   Hawai
##print('Ha ' + 'Ha ' + 'Ha ') =   Ha Ha Ha 
##print('Ha' + '300')          =   Ha300
##print('19' + '300')          =   19300

##type('Hello')      =   <class 'str'>
##type(30*5)         =   <class 'int'>
##type('1996')       =   <class 'str'>
##type(32/9)         =   <class 'float'>

##print(16+2**3)         =   2**3
##                       =   8
##                       =   16+8
##                       =   24

##important number
## ()    **  [* / // %]  [+ -]

##print('Welcome!!!')
##x = 5
##y = 4
##print(x)
##x = 3
##print(x * y)

##print('Welcome!!!')
##x = 5
##y = 4
##print(x)
##x = x - 3
##print(x * y)

##''''''Do not Python'''''''
##and	assert	break	class	continue    def	        del	yield
##elif	else	if	except	exec	    finally	for
##from	global	import	in	is	    lambda	not
##or	pass	print	raise	try	    while	with

##name = input('Please enter your name:')
##print('Hello, ' + name)

##time = input('Enter time range in weeks: ')
##print('The time range is ' + (time * 7) + ' days. ')

##time_str = input('Enter time range in weeks: ')
##time = int(time_str)
##print('The time range is ' + str(time * 7) + ' days. ')

'''Exemple'''

''' ***1***


#x = input("Enter your name: ")
#y = input("Enter your birth year: ")
#z = input("Enter a year: ")
#print("Hi",x,",")
#print("In",z,"you will be",int(z)-int(y),"years old.")

'''


''' ***2***


#x = float(input("Enter the temperature in Calsius: "))
#F = ((9/5)*float(x)+32)
#print("The temperature is",F,'degree Fahrenheit.')

'''



''' ***3.1***


#print("Welcome to Change Calculator.")
#box =[500,100,50,20,10,5,2,1]
#a = int(input("\nPrice: "))
#b = int(input("\nAmount tendered: "))
#c= b-a
#print('\nChange:',b-a)
#i=0
#while(i<8):
#  #if(c//box[i]!=0): เอาเฉพาะธนบัตรที่ต้องทอน
#    print(box[i],":",c//box[i])
#    c-=box[i]*(c//box[i])
#    i+=1
#print("\nThank you.")
#เขียน for ด้วย

'''



''' ***3.2***


#print("Welcome to Change Calculator.")
#a=input("\nPrice: ")
#b=int(a)
#c=input("\nAmount tendered: ")
#d=int(c)
#e=d-b
#f=input("\nChange: "+str(e))
#oat1= input("500: "+str(e//500))
#o1= e%500
#oat2= input("100: "+str(o1//100))
#o2= o1%100
#oat3= input("50: "+str(o2//50))
#o3= o2%50
#oat4= input("20: "+str(o3//20))
#o4= o3%20
#oat5= input("10: "+str(o4//10))
#o5= o4%10
#oat6= input("5: "+str(o5//5))
#o6= o5%5
#oat7= input("2: "+str(o6//2))
#o7=o6%2
#oat8= input("1: "+str(o7//1))
#o8= o7%1
#print("\nThank you.")

'''

