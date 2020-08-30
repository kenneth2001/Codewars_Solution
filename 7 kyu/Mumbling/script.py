def accum(s):
    return "-".join((i * c).title() for i, c in enumerate(s, 1))
