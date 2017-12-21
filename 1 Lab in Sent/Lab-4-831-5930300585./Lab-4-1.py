''' ***1

def remove_spaces(z):
    return z.replace(" ","")

'''



''' ***2

def binary_string(z):
    if z == 0:
        return '0'
    if z > 0:
        return ("{0:b}".format(z))

'''


''' ***3

def use_all_aeiou(z):
    if 'a' in z and 'e' in z and 'i' in z and 'o' in z and 'u' in z:
        return True
    else:
        return False

'''



''' ***4

def count_word(w,s):
    count = 0
    for i in range(len(s)-len(w)):
        check = 1
        for j in range(len(w)):
                if (w[j] != s[i+j]):
                    check = 0
                    break
        if(check == 1):
            count += 1
    return count

'''



''' ***5

def older_name(z1, z2):
#order_name(('name1', (d1, m1, y1)),('name2', (d2 ,m2, y2)))
#day = d
#mouth = m
#year = y
    name1, birth1 = z1
    name2, birth2 = z2
    d1, m1, y1    =birth1
    d2, m2, y2    =birth2
    if y2 < y1:
        return name2
    elif y2 > y1:
        return name1
    else:
        if m1 < m2:
            return name1
        elif m1 > m2:
            return name2
        else:
            if d1 <= d2:
                return name1
            else:
                return name2

'''
