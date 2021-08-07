"Function attributes"
'''
don’t have a nonlocal statement—or you want your code to work portably on both 3.X and 2.X—you may still 
be able to avoid globals and classes by making use of function attributes for some changeable state instead.
'''

def tracer(func):                                       # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):                       # calls is per-function, not global
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@tracer
def spam(a, b, c):                                      # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                                         # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                                           # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)                                     # wrapper calls spam

eggs(2, 16)                                             # Really calls wrapper, assigned to eggs
eggs(4, y=4)                                            # wrapper.calls _is_ per-decoration here


'''
this works only because the name wrapper is retained in
the enclosing tracer function’s scope. When we later increment wrapper.calls, we are
not changing the name wrapper itself, so no nonlocal declaration is required.
'''


"""
However, function attributes also have substantial advantages. For one, they allow
access to the saved state from outside the decorator’s code; nonlocals can only be seen
inside the nested function itself, but function attributes have wider visibility. For another,
they are far more portable; this scheme also works in 2.X, making it versionneutral.

Because decorators often imply multiple levels of callables, you can combine functions
with enclosing scopes, classes with attributes, and function attributes to achieve a variety
of coding structures. As we’ll see later, though, this sometimes may be subtler
than you expect—each decorated function should have its own state, and each decorated
class may require state both for itself and for each generated instance.
"""
