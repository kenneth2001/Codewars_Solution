def next_bigger(n):
    k = sorted(str(n))
    t = int("".join(sorted(str(n), reverse=True)))
    if t == n:
        return -1
    for num in range(n+1, t+1):
        if sorted(str(num)) == k:
            return num

# OLD VERSION     
# from itertools import permutations
# def next_bigger(n):
#     k = list(str(n))
#     if int("".join(sorted(str(n), reverse=True))) == n:
#         return -1
#     lst = sorted(list(set(permutations(sorted(k, reverse=True)))))
#     idx = lst.index(tuple(k))
#     ele = int("".join(lst[idx+1]))
#     return ele