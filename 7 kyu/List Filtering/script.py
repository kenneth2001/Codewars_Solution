def filter_list(l):
    lst = []
    for temp in l:
        if type(temp) == int:
            lst.append(temp)
    return lst
