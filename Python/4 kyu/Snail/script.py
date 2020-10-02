def snail(array):
    a = []
    while array:
        a += list(array.pop(0))
        array = list(zip(*array))
        array.reverse()
    return a
