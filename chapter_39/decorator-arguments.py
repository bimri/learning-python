"Decorator Arguments"
'''
Both function and class decorators can also seem to take arguments, although really
these arguments are passed to a callable that in effect returns the decorator, which in
turn returns a callable. By nature, this usually sets up multiple levels of state retention.
The following, for instance:
'''
@decorator(A, B)
def F(arg):
    ...

F(99)

'''
is automatically mapped into this equivalent form, where decorator is a callable that
returns the actual decorator. The returned decorator in turn returns the callable run
later for calls to the original function name:
'''
def F(arg):
    ...

F = decorator(A, B)(F)                              # Rebind F to result of decorator's return value
F(99)                                               # Essentially calls decorator(A, B)(F)(99)


'''
Decorator arguments are resolved before decoration ever occurs, and they are usually
used to retain state information for use in later calls. The decorator function in this
example, for instance, might take a form like the following:
'''
def decorator(A, B):
    # Save or use A, B
    def actualDecorator(F):
        # Save or use function F
        # Return a callable: nested def, class with __call__, etc.
        return callable
    return actualDecorator


""" 
The outer function in this structure generally saves the decorator arguments away as
state information, for use in the actual decorator, the callable it returns, or both. This
code snippet retains the state information argument in enclosing function scope references,
but class attributes are commonly used as well.

In other words, decorator arguments often imply three levels of callables: a callable to
accept decorator arguments, which returns a callable to serve as decorator, which returns
a callable to handle calls to the original function or class. Each of the three levels
may be a function or class and may retain state in the form of scopes or class attributes.
"""


'''
Decorator arguments can be used to provide attribute initialization values, call trace
message labels, attribute names to be validated, and much more—any sort of configuration
parameter for objects or their proxies is a candidate.
'''


'Decorators Manage Functions and Classes, Too'
'''
it’s important to remember that the decorator mechanism is more general
than this—it is a protocol for passing functions and classes through any callable immediately
after they are created
'''
def decorator(O):
    # save or augment function or class O
    return O 

@decorator
def F(): ...                        # F = decorator(F)

@decorator
class C: ...                        # C = decorator(C)
