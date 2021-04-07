def snail(snail_map):
    array = []
    while len(snail_map) != 0:
        temp = []
        if len(snail_map) != 0:
            array += snail_map.pop(0)
        if len(snail_map) != 0:
            for i in range(len(snail_map)):
                array += [snail_map[i].pop(-1)]
        if len(snail_map) != 0:
            array += reversed(snail_map.pop(-1))
        if len(snail_map) != 0:
            for i in range(len(snail_map)):
                temp += [snail_map[i].pop(0)]
            array += reversed(temp)
    return array
