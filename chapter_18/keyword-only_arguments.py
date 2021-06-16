'''
keyword-only arguments are coded as named arguments 
that may appear after in the arguments list *args
'''
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
kwonly(a=1, c=3)
kwonly(1,2,3,4,5,6,c=9)

"TypeError: kwonly() missing 1 required keyword-only argument: 'c'"
# kwonly(1,2,3)


'''
We can also use a * character by itself in the arguments list to indicate that a function
does not accept a variable-length argument list but still expects all arguments following
the * to be passed as keywords. In the next function, a may be passed by position or
name again, but b and c must be keywords, and no extra positionals are allowed:
'''
def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)
kwonly(c=30, b=20, a=100)

"TypeError: kwonly() takes 1 positional argument but 3 were given"
# kwonly(1, 2, 3)

"TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'"
# kwonly(1)


'''
You can still use defaults for keyword-only arguments, even though they appear after
the * in the function header.
'''
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)

"TypeError: kwonly() takes 1 positional argument but 2 were given"
# kwonly(1, 2)


'''
keyword-only arguments with defaults are optional, but those without defaults
effectively become required keywords
'''
def kwonly(a, *, b, c='spam'):
    print(a, b, c)

kwonly(1, b='eggs')

"TypeError: kwonly() missing 1 required keyword-only argument: 'b'"
# kwonly(1, c='eggs')

"TypeError: kwonly() takes 1 positional argument but 2 were given"
# kwonly(1, 2)


def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)

kwonly(3, c=4)
kwonly(3, c=4, b=5)

"TypeError: kwonly() missing 1 required keyword-only argument: 'c'"
# kwonly(3)

"TypeError: kwonly() takes 1 positional argument but 3 were given"
# kwonly(1, 2, 3)
