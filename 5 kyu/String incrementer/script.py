def increment_string(string):
    word_of_string = string.rstrip("0123456789")
    word_of_integer = string[len(word_of_string):]
    if word_of_integer == "":
        return word_of_string + "1"
    return word_of_string + str(int(word_of_integer) + 1).zfill(len(word_of_integer))
