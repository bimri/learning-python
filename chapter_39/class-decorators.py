"Class Decorators"
'''
Class decorators are strongly related to function decorators; in fact, they use the same
syntax and very similar coding patterns. Rather than wrapping individual functions or
methods, though, class decorators are a way to manage classes, or wrap up instance
construction calls with extra logic that manages or augments instances created from a
class. In the latter role, they may manage full object interfaces.
'''

'Usage'
"""
The net effect is that calling the class name later to create an instance winds up triggering
the callable returned by the decorator, which may or may not call the original class itself.
"""
@decorator                      # Decorate class
class C:
    ...

x = C(99)                       # Make an instance

# equivalent to the following
class C:
    ...

C = decorator(C)                # Rebind class name to decorator result
x = C(99)                       # Essentially calls decorator(C)(99)  


'Implementation'
'''
New class decorators are coded with many of the same techniques used for function
decorators, though some may involve two levels of augmentation—to manage both
instance construction calls, as well as instance interface access.
'''
# decorator’s result is what runs when an instance is later created.
def decorator(C):
    # Process class C
    ...
    return C

@decorator
class C: ...                    # C = decorator(C)

'To instead insert a wrapper layer that intercepts later instance creation calls, return a different callable object:'
def decorator(C):
    # Save or use class C
    # Return a different callable: nested def, class with __call__, etc.
    ...

@decorator
class C: ...                    # C = decorator(C)


"""
The callable returned by such a class decorator typically creates and returns a new
instance of the original class, augmented in some way to manage its interface.
"""
def decorator(cls):                                     # On @ decoration
    class Wrapper:
        def __init__(self, *args):                      # On instance creation
            self.wrapped = cls(*args)
        def __getattr__(self, name):                    # On attribute fetch
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:                                                # C = decorator(C)
    def __init__(self, x, y):                           # Run by Wrapper.__init__
        self.attr = 'spam'

x = C(6, 7)                                             # Really calls Wrapper(6, 7)
print(x.attr)                                           # Runs Wrapper.__getattr__, prints "spam"


'''
In this example, the decorator rebinds the class name to another class, which retains
the original class in an enclosing scope and creates and embeds an instance of the
original class when it’s called. When an attribute is later fetched from the instance, it
is intercepted by the wrapper’s __getattr__ and delegated to the embedded instance
of the original class. Moreover, each decorated class creates a new scope, which remembers
the original class.
'''


"""
Like function decorators, class decorators are commonly coded as either “factory”
functions that create and return callables, classes that use __init__ or __call__ methods
to intercept call operations, or some combination thereof. Factory functions typically
retain state in enclosing scope references, and classes in attributes.
"""


'Supporting multiple instances'
class Decorator:
    def __init__(self, C):                          # On @ decoration
        self.C = C
    def __call__(self, *args):                      # On instance creation
        self.wrapped = self.C(*args)
        return self
    def __getattr__(self, attrname):                # On atrribute fetch
        return getattr(self.wrapped, attrname)

@Decorator
class C: ...                                        # C = Decorator(C)

x = C()
y = C()                                             # Overwrites x!


# following patterns supports multiple wrapped instances:
def decorator(C):                                   # On @ decoration
    class Wrapper:
        def __init__(self, *args):                  # On instance creation: new Wrapper
            self.wrapped = C(*args)                 # Embed instance in instance
        return Wrapper

class Wrapper: ...
def decorator(C):                                   # On @ decoration
    def onCall(*args):                              # On instance creation: new Wrapper
        return Wrapper(C(*args))                    # Embed instance in instance
    return onCall
