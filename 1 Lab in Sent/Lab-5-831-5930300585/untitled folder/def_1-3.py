
''' ***Lab5-(1-3)
##1


#def intersect(a, b):
#return the intersection of two lists """
#    return list(set(a) & set(b))


#def intersect(seq1, seq2):
#    empty = []                     # start empty
#    for x in seq1:                 # scan seq1
#        if x in seq2:              # common item?
#            empty.append(x)        # add to end
#    return empty


###2

#def transpose(matrix):
#   x=0
#   trans=[]
#   b=len(matrix[0])
#   while b!=0:
#       trans.append([])
#       b-=1
#   for list in matrix:
#       for element in list:
#          trans[x].append(element)
#          x+=1
#       x=0
#   return trans

#m = []
#def transpose(m):
#    if not m: return []
#    return [[row[i]for row in m] for i in range (len(m[0]))]

###3

#a = []
#b = []
#def multiply(a, b):
#    c =[[0 for row in range(len(a))] for col in range(len(b[0]))]
#    for i in range(len(a)):
#        for j in range(len(b[0])):
#            for k in range(len(b)):
#                c[i][j] += a[i][k]*b[k][j]
#    return c

