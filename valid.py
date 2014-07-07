'''
Created on 2014-2-9

@author: King
'''
# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

import string, re, itertools
import __future__

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here 
    for f in fill_in(formula):
        if valid(f):
            return f
    
def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
    
# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if str.isalpha(word) and str.isupper(word):
        res_alp = ''
        for i in range(1, len(word)):
            res_alp += (str(10 ** (i-1)) + '*' + word[-i] + '+')
        res_alp += (str(10 ** (len(word) - 1)) + '*' + word[0])
        return res_alp
    else:
        return word

def y_compile_word(word):
    if word.isupper():
        terms = [('%s*%s') % (10**i, d)
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms)+ ')'
    else:
        return word


