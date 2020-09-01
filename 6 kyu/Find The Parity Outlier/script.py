def find_outlier(integers):
    odd = []
    even = []
    for num in integers:
        if num % 2 == 0:
            odd.append(num)
        else:
            even.append(num)
    return odd.pop() if len(odd) == 1 else even.pop()
