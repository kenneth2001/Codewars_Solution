def longest_slide_down(pyramid):
    value = pyramid.pop()
    while pyramid:
        temp = pyramid.pop()
        value = [temp[i] + max(value[i],value[i+1]) for i in range(len(temp))]
    return value.pop()
