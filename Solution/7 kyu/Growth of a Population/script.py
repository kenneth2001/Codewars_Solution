def nb_year(p0, percent, aug, p):
    ans = 0
    while p0 < p:
        ans += 1
        p0 = int(p0 * (1 + percent / 100) + aug)
    return ans