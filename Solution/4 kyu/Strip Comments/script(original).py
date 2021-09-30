def solution(string,markers):
    s = string.split("\n")
    result = ""
    for line in s:
        trimmed = ""
        for c in line:
            if c not in markers:
                trimmed += c
            else:
                break
        trimmed = trimmed.rstrip()
        result = result + trimmed + "\n"
    return result[:-1]

print("hello # 123\nhello !123".split(['#', '!']))