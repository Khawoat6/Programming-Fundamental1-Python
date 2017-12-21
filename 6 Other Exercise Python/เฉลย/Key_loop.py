factor ,ans = int(input("n: ")),1
for i in range(factor):
  if(i>0):
    ans*=i
print(factor*ans)

#หรือแก้โดย
#factor ,ans = int(input("n: ")),1
#for i in range(factor+1):
#  if(i>0):
#    ans=ans*i
#print(ans)
