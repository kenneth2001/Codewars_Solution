from functools import reduce
def persistence(n):
    count = 0
    while n >= 10:
        n = reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        count += 1
    return count
