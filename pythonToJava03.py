
def binary_search( lst, v ):
    i, j = 0 , len( lst )
    while i < j:
        mid = ( i+j ) / 2
        if v < lst[ mid ]:
            j = mid
        elif v > lst[mid]:
            i = mid + 1
        else:
            return mid
    return None
'''

lst = [ 1, 2, 3, 2, 5, 3, 1, 3, 9 ]
i = 0
while i < len( lst ):
    if lst[i] % 3 == 0 :
        lst.pop(i)      # remove + return value remove

    else:
        i = i + 1
print (lst)
