def solution(s):
    string = ""
    for character in s:
        string += "{0}{1}".format(" " if character.isupper() else '', character)
    return string
