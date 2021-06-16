"Headers: Collecting arguments"
def f(*args): print(args)

'Python collects all the positional arguments into a new tuple'
f()
f(1)
f(1,3,4,78)


'** works only for keyword arguments; collects them into a dict'
'the ** form allows you to convert from keywords to dictionaries'
'which you can then step through with calls, keys'
def f(**args): print(args)

f()
f(a=1, b=2)


'''
Function headers can combine normal arguments, the *, 
and the ** to implement wildly flexible call signatures
'''
def f(a, *pargs, **kargs): print(a, pargs, kargs)

f(1)
f(1, 2, 3, x=1, y=2)


"Calls: Unpacking arguments"
# * at call of a function
#  means - unpacking a collection of arguments
def func(a, b, c, d): print(a, b, c, d)

args = (1, 3)
args += (8, 90)

func(*args)                                 # Same as func(1, 2, 3, 4)


# ** syntax in a function call
# unpacks a dictionary key/value pairs
args = {'a': 'rio', 'b': 'las', 'c': 'vancouver'}
args['d'] = 4

func(**args)


"COMBINATION, normal, positional, keyword arguments"
func(*(1, 2), **{'d': 4, 'c': 3})               # same as func(1,2,d=4, c=3)
func(1, *(2, 3), **{'d': 4})                    # Same as func(1, 2, 3, d=4)
func(1, c=3, *(2,), **{'d': 4})                 # Same as func(1, 2, c=3, d=4)
func(1, *(2, 3), d=4)                           # Same as func(1, 2, 3, d=4)
func(1, *(2,), c=3, **{'d':4})                  # Same as func(1, 2, c=3, d=4)

'don’t confuse the */** starred-argument syntax in the function header and the function call'
