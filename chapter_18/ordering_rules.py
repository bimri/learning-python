"note that keyword-only arguments must be specified after a single star, not two"

'SyntaxError: invalid syntax'
# def kwonly(a, **pargs, b, c): ...

'SyntaxError: invalid syntax'
# def kwonly(a, **, b, c):


# SyntaxError: invalid syntax
"Keyword-only before **!"
# def f(a, *b, **d, c=6): print(a, b, c, d)



def f(a, *b, c=6, **d): print(a, b, c, d)               # Collect args in header

f(1, 2, 3, x=4, y=5)                                    # Defaults used

f(1, 2, 3, x=4, y=5, c=7)                               # Override default

f(1, 2, 3, c=7, x=4, y=5)                               # Anywhere in keywords

'''
when keyword-only arguments are passed, they must appear before a
**args form. The keyword-only argument can be coded either before or after the
*args, though, and may be included in **args:
'''
def f(a, *b, c=6, **d): print(a, b, c, d)                           # KW-only between * and **

f(1, *(2, 3), **dict(x=4, y=5))                                     # Unpack args at call

"SyntaxError: invalid syntax"
# f(1, *(2, 3), **dict(x=4, y=5), c=7)                                # Keywords before **args!

f(1, *(2, 3), c=7000, **dict(x=4, y=5))                               # Override default
f(1, c=700, *(2, 3), **dict(x=4, y=5))                                # After or before *
f(1, *(2, 3), **dict(x=4, y=5, c=70))                                 # Keyword-only in **


"Why keyword-only arguments?"
'''
process(X, Y, Z)                                                    # Use flag's default
process(X, Y, notify=True)                                          # Override flag default
'''