def make_readable(seconds):
    return "{:02}:{:02}:{:02}".format(seconds//3600, seconds//60%60, seconds%60)
