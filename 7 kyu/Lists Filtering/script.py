# Description
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    lst = []
    for temp in l:
        if type(temp) == int:
            lst.append(temp)
    return lst

# Test
"""
print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
"""
