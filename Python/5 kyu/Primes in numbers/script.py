def primeFactors(n):
    factor = 2
    result = ""
    temp = 0
    while n != 1:
        while n % factor == 0:
            n = n / factor
            temp += 1
        if temp >= 1:
            result += "({}{})".format(factor, "**" + str(temp) if temp > 1 else "")
        factor += 1
        temp = 0
    return result
