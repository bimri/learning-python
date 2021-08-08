"Decorators Versus Manager Functions"
# use Python’s introspection facilities to fetch the class from an
# already created instance
class Person: ...


instances = {}
def getInstance(object):
    aClass = object.__class__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40, 10))                                # Versus: bob = Person('Bob', 40, 10)


'''
The same holds true for function decorators like the tracer we wrote earlier: rather than
decorating a function with logic that intercepts later calls, we could simply pass the
function and its arguments into a manager that dispatches the call:
'''
def func(x, y):                                     # Nondecorator version
    ...                                             # def tracer(func, args): ... func(*args(
result = tracer(func, (1, 2))                       # Special call syntax

@tracer
def func(x, y):                                     # Decorator version
    ...                                             # Rebinds name: func = tracer(func)
result = func(1, 2)                                 # Normal call syntax


'''
Manager function approaches like this place the burden of using special syntax on
calls, instead of expecting decoration syntax at function and class definitions, but also
allow you to selectively apply augmentation on a call-by-call basis.
'''
