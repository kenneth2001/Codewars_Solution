def high_and_low(numbers):
    lst = [int(item) for item in numbers.split()]
    return str(max(lst)) + " " + str(min(lst))
