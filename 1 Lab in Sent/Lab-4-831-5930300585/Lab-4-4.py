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
