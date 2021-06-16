from __future__ import print_function
from functools import reduce
from timeit import repeat
import math

def fact0(N):                                                                                           # Recursive
    if N == 1:                                                                                          # Fails at 999 by default
        return N
    else:
        return N * fact0(N-1)

def fact1(N):
    return N if N == 1 else N * fact1(N-1)                                                              # Recursive, one-liner

def fact2(N):                                                                                           # Functional
    return reduce(lambda x, y: x * y, range(1, N+1))

def fact3(N):
    res = 1
    for i in range(1, N+1): res *= i                                                                    # Iterative
    return res

def fact4(N):
    return math.factorial(N)                                                                            # Stdlib "batteries"

# Tests
print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6))                                                 # 6*5*4*3*2*1: all 720
print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))                               # True

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))



'''
Conclusions: recursion is slowest on my Python and machine, and fails once N
reaches 999 due to the default stack size setting in sys;

this limit can be increased, but simple loops or the standard library tool seem the best route
here in any event

recursion is today an order
of magnitude slower in CPython, though these results vary in PyPy:
'''
def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1]) # Recursive: 10x slower in CPython today

def rev2(S):
    return ''.join(reversed(S)) # Nonrecursive iterable: simpler, faster

def rev3(S):
    return S[::-1] # Even better?: sequence reversal by slice
