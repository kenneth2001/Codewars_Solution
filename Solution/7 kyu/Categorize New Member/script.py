def open_or_senior(data):
    return ['Senior' if mem[0] >= 55 and mem[1] > 7 else 'Open' for mem in data]