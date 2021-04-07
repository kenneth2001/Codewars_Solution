def move_zeros(array):
    for i in range(0, array.count(0)):
        array.pop(array.index(0))
        array.append(0)
    return array
