def DNA_strand(dna):
    my_table = str.maketrans("ATCG", "TAGC")
    return dna.translate(my_table)

#def DNA_strand(dna):
    #return dna.translate(str.maketrans('ATCG', 'TAGC')) 
