from math import factorial as fac
def factorial(n):
    if n > 12 or n < 0:
        raise ValueError
    return fac(n)
