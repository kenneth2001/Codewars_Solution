# Description 
"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
"""

def tickets(people):
    cash_25 = 0
    cash_50 = 0
    for temp in people:
        if temp == 25:
            cash_25 += 1
        elif temp == 50:
            cash_25 -= 1
            cash_50 += 1
            if cash_25 < 0:
                return "NO"
        elif temp == 100:
            if cash_25 >=1 and cash_50 >= 1:
                cash_25 -= 1
                cash_50 -= 1
            elif cash_25 >= 3:
                cash_25 -= 3
            else:
                return "NO"    
    return "YES"
    
  # Test
  """
  print(ticket([25, 25, 50]))  --> output: YES
  print(ticket([25, 100]))  --> output: NO
"""
