def solution(number):
    return sum([num for num in range(3, number) if num % 3 == 0 or num % 5 == 0])
