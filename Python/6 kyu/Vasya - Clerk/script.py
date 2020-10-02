def tickets(people):
    cash_25 = 0
    cash_50 = 0
    for temp in people:
        if temp == 25:
            cash_25 += 1
        elif temp == 50:
            cash_25 -= 1
            cash_50 += 1
            if cash_25 < 0:
                return "NO"
        elif temp == 100:
            if cash_25 >=1 and cash_50 >= 1:
                cash_25 -= 1
                cash_50 -= 1
            elif cash_25 >= 3:
                cash_25 -= 3
            else:
                return "NO"    
    return "YES"
