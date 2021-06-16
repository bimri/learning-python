def f1(a, b): print(a, b)                                       # Normal args
def f2(a, *b): print(a, b)                                      # Positional varargs
def f3(a, **b): print(a, b)                                     # Keyword varargs
def f4(a, *b, **c): print(a, b, c)                              # Mixed modes
def f5(a, b=2, c=3): print(a, b, c)                             # Defaults
def f6(a, b=2, *c): print(a, b, c)                              # Defaults and positional varargs


'''
% python
>>> f1(1, 2)                                                    # Matched by position (order matters)
1 2

>>> f1(b=2, a=1)                                                # Matched by name (order doesn't matter)
1 2

>>> f2(1, 2, 3)                                                 # Extra positionals collected in a tuple
1 (2, 3)

>>> f3(1, x=2, y=3)                                             # Extra keywords collected in a dictionary
1 {'x': 2, 'y': 3}

>>> f4(1, 2, 3, x=2, y=3)                                       # Extra of both kinds
1 (2, 3) {'x': 2, 'y': 3}

>>> f5(1)                                                       # Both defaults kick in
1 2 3

>>> f5(1, 4)                                                    # Only one default used
1 4 3

>>> f6(1)                                                       # One argument: matches "a"
1 2 ()

>>> f6(1, 3, 4)                                                 # Extra positional collected
1 3 (4,)
'''