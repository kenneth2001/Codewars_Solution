def sum_of_intervals(intervals):
    lst = []
    for array in intervals:
        for num in range(array[0], array[1]):
            if num not in lst:
                lst.append(num)
    return len(lst)
