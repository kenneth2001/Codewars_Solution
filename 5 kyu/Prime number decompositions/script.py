def getAllPrimeFactors(n):
    if type(n) != int or n <= 0: return []
    if n == 1: return [1]
    array = []
    k = 2
    while n != 1:
        if n % k == 0:
            n /= k
            array.append(k)
        else:
            k += 1
    return array


def getUniquePrimeFactorsWithCount(n):
    array = getAllPrimeFactors(n)
    if array == []: return [[], []]
    unique = []
    count = []
    for num in array:
        if num not in unique:
            unique.append(num)
            count.append(array.count(num))
    return [unique] + [count]


def getUniquePrimeFactorsWithProducts(n):
    array = getUniquePrimeFactorsWithCount(n)
    if array == [[], []]: return []
    if n <= 2: return [n]
    product = []
    for i in range(len(array)):
        product.append(array[0][i]**array[1][i])
    return product
