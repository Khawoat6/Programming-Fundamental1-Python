m1 = [[1,1],[1,1]]
m2 = [[1,1],[1,1]]
x , y   = [],[]
for i in range(2):
  for j in range(2):
    y.append(m1[i][j]+m2[i][j])
  x.append(y)
print('ans =',y)

    
