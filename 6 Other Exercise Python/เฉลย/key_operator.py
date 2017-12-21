print("Welcome to Change Calculator.")
box =[500,100,50,20,10,5,2,1]
a = int(input("Price: "))
b = int(input("Amount tendered: "))
c= b-a
print('Change:',b-a)
i=0
while(i<8):
  #if(c//box[i]!=0): เอาเฉพาะธนบัตรที่ต้องทอน
    print(box[i],":",c//box[i])
    c-=box[i]*(c//box[i])
    i+=1
print("Thank you.")

#เขียน for ด้วย
