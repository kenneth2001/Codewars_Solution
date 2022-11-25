def longest(a1, a2):
    from string import ascii_lowercase
    return "".join([x for x in ascii_lowercase if x in a1 or x in a2])
