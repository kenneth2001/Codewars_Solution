def valid_parentheses(string):
    counter = 0
    for c in string:
        if c == "(":
            counter += 1
        if c == ")":
            counter -= 1
        if counter < 0:
            return False
    return True if counter == 0 else False