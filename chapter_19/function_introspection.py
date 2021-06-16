def func(a):
    b = 'amapiano'
    return b * a

print(func(5))


'''
call expression is just one operation defined to work on function 
objects. We can also inspect their attributes generically
'''

print(func.__name__)
print(dir(func))


# Introspection tools allow us to explore implementation details
print(func.__code__)

print(dir(func.__code__))
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
