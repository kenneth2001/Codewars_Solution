def printer_error(s):
    return f"{len([x for x in s if x in 'nopqrstuvwxyz'])}/{len(s)}"