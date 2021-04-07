import string
def duplicate_count(text):
    return sum([1 if text.lower().count(str(i)) > 1 else 0 for i in list(string.ascii_lowercase)+list(range(0,10))])
