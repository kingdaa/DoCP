'''
Created on 2014-2-16

@author: King
'''

s = 'aaaabbbbbbbcc'
ss = set([s])
sss = set([s]) | set([s+'a'])
print sss

aa = 'abcdefg'
pre = 'abc'
print tuple(pre)

print aa.startswith(tuple(pre))
print list(pre)

print '/>'
print '\"'

xmatches = set(range(1,5))
print xmatches

def aha(f):
    print 'heihou: ' + str(type(f))
    return f

@aha
def ri(a, b):
    return a+b

print ri(1,2)
print help(ri)
