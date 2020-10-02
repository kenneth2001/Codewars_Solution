from itertools import product
def rolldice_sum_prob(target, dice_amount):
    case =  [sum(item) for item in product([1, 2, 3, 4, 5, 6], repeat = dice_amount)]
    return case.count(target) / len(case)
