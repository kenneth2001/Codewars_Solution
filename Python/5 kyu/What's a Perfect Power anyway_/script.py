from math import log, sqrt

def isPP(n):
    for k in range(2, round(sqrt(n)+1)):
        if k ** round(log(n, k)) == n:
            return [k, round(log(n, k))]
    return None
