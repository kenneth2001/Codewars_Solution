def count_bits(n):
    return bin(n).replace('0b', '').count('1')