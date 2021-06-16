"annotation information"
# arbitrary user-defined data about a function’s 
# arguments and result—to a function object

'annotations are completely optional'
#attached to the function object's __annotations__ attribute
# e.g. use annotations in the context of error testing
def func(a, b, c):
    return a + b + c 

print(func(2, 3, 4))


# Syntactically, function annotations are code in def header lines
# associated with arguments and return values
def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(func(1,2,3))


'''
when annotations are present Python
collects them in a dictionary and 
attaches it to the function object itself
'''
print(func.__annotations__)

def func(a: 'spam', b, c: 99):
    return a + b + c

print(func(1,3,4))
print(func.__annotations__)


for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


'''
you can still use defaults for arguments if
you code annotations—the annotation (and its : character) appear before the default
(and its = character).
'''
def func(a: 'spam' = 4, b: (1,10) = 5, c: float =6) -> int:
    return a + b + c 

print(func(1,2,3))
print(func())                                       # 4 + 5 + 6 (all defaults)
print(func(1, c=10))                                # 1 + 5 + 10 (keyword work normally)
print(func.__annotations__)


'''
note that annotations work only in def statements, 
not lambda expressions
'''