def intersect(a, b):
    empty = []                     # start empty
    for x in a:                    # scan a
        if x in b:                 # common item?
            empty.append(x)        # add to end
    else:                          # not x in a and b 
        return empty
