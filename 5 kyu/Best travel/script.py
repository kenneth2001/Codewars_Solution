from itertools import combinations
def choose_best_sum(t, k, ls):
    return max((num for num in (sum(pack) for pack in combinations(ls, k)) if num <= t) , default=None)
