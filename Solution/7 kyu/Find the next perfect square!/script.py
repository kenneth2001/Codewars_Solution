def find_next_square(sq):
    return -1 if not (sq**0.5).is_integer() else (sq ** 0.5 + 1) ** 2
