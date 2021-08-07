"The Basics"
'Function Decorators'
'''
Most of the magic of decorators boils down to an automatic rebinding operation.
They are largely just syntactic sugar that runs one function through another
at the end of a def statement, and rebinds the original function name to the result.
'''


"""
Usage

A function decorator is a kind of runtime declaration about the function whose definition
follows. The decorator is coded on a line just before the def statement that defines
a function or method, and it consists of the @ symbol followed by a reference to a
metafunction—a function (or other callable object) that manages another function.
"""
@decorator                  # Decorate function
def F(arg):
    ...

F(99)                       # Call function


# equivalent form
def F(arg):
    ...
F = decorator(F)            # Rebind function name to decorator result

F(99)

'''
This automatic name rebinding works on any def statement, whether it’s for a simple
function or a method within a class. When the function F is later called, it’s actually
calling the object returned by the decorator, which may be either another object that
implements required wrapping logic, or the original function itself.

In other words, decoration essentially maps the first of the following into the second
—though the decorator is really run only once, at decoration time:
    func(6, 7)
    decorator(func)(6, 7)
'''


"""
This automatic name rebinding accounts for the static method and property decoration
syntax. In both cases, the method name is rebound to the result of a built-in function decorator,
at the end of the def statement. Calling the original name later invokes whatever object
the decorator returns. In these specific cases, the original names are rebound to a static
method router and property descriptor, but the process is much more general than this.
"""
class C:
    @staticmethod
    def meth(): ...            # meth = staticmethod(meth)

class C:
    @property
    def name(self): ...         # name = property(name)



'Implementation'
# A decorator itself is a callable that returns a callable.

def decorator(F):
    # Process function F
    return F

@decorator
def func(): ...                 # func = decorator(func)


# a proxy for later calls:

def decorator(F):
    # Save or use function F
    # Return a different callable: nested def, class with __call__, etc.
    ...

@decorator
def func(): ...                 # func = decorator(func)


# decorator returns a wrapper that retains the original function in an enclosing scope
def decorator(F):               # On @ decoration
    def wrapper(*args):         # On wrapped function
        # Use F and args
        # F(*args) calls original function
        ...
    return wrapper

@decorator
def func(x, y):                 # func = decorator(func)
    ...                         # func is passed to decorator's F

func(6, 7)

'''
When the name func is later called, it really invokes the wrapper function returned by
decorator; the wrapper function can then run the original func because it is still available
in an enclosing scope. When coded this way, each decorated function produces a new
scope to retain state.
'''


"""
To do the same with classes, we can overload the call operation and use instance attributes
instead of enclosing scopes:

When the name func is later called now, it really invokes the __call__ operator overloading
method of the instance created by decorator; the __call__ method can then
run the original func because it is still available in an instance attribute. When coded
this way, each decorated function produces a new instance to retain state.
"""
class decorator:
    def __init__(self, func):                   # On @ decoration
        self.func - func 
    def __call__(self, *args):                  # On wrapped function call
        # Use self.func and args
        # self.func(*args) calls origical function
        ...
    
@decorator
def func(x, y):                                 # func = decorator(func)
    ...                                         # func is passed to __init__

func(5, 7)                                      # 6, 7 are passed to __call__'s args


'Supporting method decoration'
class decorator:
    def __init__(self, func):                   # func is method without instance
        self.func - func 
    def __call__(self, *args):                  # self is decorator instance
        # self.func(*args) fails!               # C instance not in args!
        ...
    
class C:
    @decorator
    def method(self, x, y):                     # method = decorator(method)
        ...                                     # Rebound to decorator instance
  

# To support both functions and methods, the nested function alternative works better
def decorator(F):                               # F is func or method without instance
    def wrapper(*args):                         # class instance in args[0] for method
                                                # F(*args) runs func or method
        ...                                                
    return wrapper

@decorator
def func(x, y):                                 # func = decorator(func)
    ...

func(6, 7)                                      # Really calls wrapper(6, 7)

class C:
    @decorator
    def method(self, x, y):                     # method = decorator(method)
        ...                                     # Rebound to simple function

X = C()
X.method(6, 7)                                  # Really calls wrapper(X, 6, 7)


'''
Technically, this nested-function version works because Python creates a bound
method object and thus passes the subject class instance to the self argument only
when a method attribute references a simple function; when it references an instance
of a callable class instead, the callable class’s instance is passed to self to give the
callable class access to its own state information.

Also note that nested functions are perhaps the most straightforward way to support
decoration of both functions and methods, but not necessarily the only way.
'''
