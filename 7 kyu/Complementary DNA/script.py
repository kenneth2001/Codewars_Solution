# Description
'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
'''

def DNA_strand(dna):
    temp = ""
    for character in dna:
        if character == "A":
            temp += "T"
        elif character == "T":
            temp += "A"
        elif character == "C":
            temp += "G"
        elif character == "G":
            temp += "C"
    return temp
    
'''
print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
'''
