'''
Created on Feb 10, 2014

@author: qinhuan
'''
# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def expandAroundCenter(s, c1, c2):
    n = len(s)
    while (c1 >= 0 and c2 <= n - 1 and s[c1] == s[c2]):
        c1 -= 1 
        c2 += 1
    return s[c1 + 1:c2], c1+1, c2

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    n = len(text)
    if n == 0: return (0,0)
    text = str.upper(text)
    max_subp = text[0]
    i, j = 0,0
    for k in range(len(text)-1):
        p1 = expandAroundCenter(text, k, k)
        if len(p1[0])>len(max_subp): 
            max_subp = p1[0]
            i,j = p1[1],p1[2]
        p2 = expandAroundCenter(text, k, k+1)
        if len(p2[0])>len(max_subp): 
            max_subp = p2[0]
            i,j = p2[1],p2[2]
    return (i,j)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()