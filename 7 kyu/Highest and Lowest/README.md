# Highest and Lowest

## Description 

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

Example:

    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
    
Notes:
- All numbers are valid Int32, no need to validate them.
- There will always be at least one number in the input string.
- Output string must be two numbers separated by a single space, and highest number is first.

## Test Cases

    "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6" -> "542 -214"
    
## Source
https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
