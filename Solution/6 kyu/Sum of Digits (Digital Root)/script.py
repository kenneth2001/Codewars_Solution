def digital_root(n):
    while len(str(n)) > 1:
        n = sum([int(num) for num in str(n)])
    return n
