def transpose(m):
   x=0
   trans=[]
   b=len(m[0])
   while b!=0:
       trans.append([])
       b-=1
   for list in m:
       for element in list:
          trans[x].append(element)
          x+=1
       x=0
   return trans
