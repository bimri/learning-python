'''
if sometest:
    action, args = func1, (1,)              # Call func1 with one arg in this case
else:
    action, args = func2, (1, 2, 3)         # Call func2 with three args here
...etc...
action(*args)                               # Dispatch generically

# >>> ...define or import func3...
# >>> args = (2,3)
# >>> args += (4,)
# >>> args
# (2, 3, 4)
# >>> func3(*args)
'''

"comes in handy for functions that test or time other functions"
def tracer(func, *pargs, **kargs):          # Accept arbitrary arguments
    print('calling', func.__name__)
    return func(*pargs, **kargs)            # Pass along arbitrary arguments

def funct(a, b, c, d):
    return a + b + c + d

print(tracer(funct, 1, 2, c=4, d=4))
