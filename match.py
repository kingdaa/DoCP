'''
Created on 2014-2-15

@author: King
'''
def match(pattern, text):
    """
    Return True if pattern appears at the start of text
    
    Please fill in the last line in this program.
    Namely: match(             ,           )

    We'll explain how we came to the code for the condition:
    elif len(pattern) > 1 and pattern[1] in '*?' in the next video lecture
    """

    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*': #op 0 or more
            return match_star(p, pat, text)
        elif op == '?':  # op 0 or 1
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                #q1
                match(pattern[1:], text[1:])) # fill in this line

def match1(p, text):
    if not text: return False
    else: return p=='.' or p==text[0]

def match_star(p, pattern, text):
    return (match(pattern, text) or (match1(p, text) and match_star(p, pattern, text[1:])))