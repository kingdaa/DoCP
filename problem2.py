'''
Created on Feb 10, 2014

@author: qinhuan
'''
#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def adjacent(p1, p2):
    return True if abs(p1 - p2) == 1 else False

def floor_puzzle():
    # Your code here
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if not (Hopper == 5 or Kay == 1 or Liskov == 5 or Liskov == 1 or Perlis < Kay or adjacent(Ritchie, Liskov) or adjacent(Kay, Liskov)):
            return list((Hopper, Kay, Liskov, Perlis, Ritchie))