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
    
    
