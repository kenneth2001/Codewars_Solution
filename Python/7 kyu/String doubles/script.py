def doubles(s):
    string = ""
    for character in s:
            string += character
            if len(string) > 1:
                if string[-2] == character:
                    string = string[:-2]  
    return string
