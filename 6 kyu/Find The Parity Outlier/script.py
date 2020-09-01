def find_outlier(integers):
    odd = [num for num in integers if num % 2 != 0]
    even = [num for num in integers if num % 2 == 0]
    return odd.pop() if len(odd) == 1 else even.pop()
