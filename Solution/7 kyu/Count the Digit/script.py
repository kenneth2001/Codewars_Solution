def nb_dig(n, d):
    temp = 0
    for num in [k*k for k in range(0, n+1)]:
        temp += int(str(num).count(str(d)))
    return temp
