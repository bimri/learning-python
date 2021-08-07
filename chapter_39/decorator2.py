"Decorator State Retention Options"
'''
Function decorators
have a variety of options for retaining state information provided at decoration time,
for use during the actual function call. They generally need to support multiple decorated
objects and multiple calls, but there are a number of ways to implement these
goals: instance attributes, global variables, nonlocal closure variables, and function
attributes can all be used for retaining state.
'''

'Class instance attributes'
class tracer:                                           # State via instance attributes
    def __init__(self, func):                           # On @ decorator
        self.calls = 0                                  # Save func for later call
        self.func  = func                               
    def __call__(self, *args, **kwargs):                # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):                  # Same as: spam = tracer(spam)
    print(a + b + c)                # Triggers tracer.__init__

@tracer
def eggs(x, y):                     # Same as: eggs = tracer(eggs)
    print(x ** y)                   # Wraps eggs in a tracer object

'''
class instance attributes to save state explicitly. Both the
wrapped function and the calls counter are per-instance information—each decoration
gets its own copy.

notice how the spam and eggs functions each have their own calls
counter, because each decoration creates a new class instance:
'''
spam(1, 2, 3)                       # Really calls tracer instance: runs tracer.__call__
spam(a=4, b=5, c=6)                 # spam is an instance attribute

eggs(2, 16)                         # Really calls tracer instance, self.func is eggs
eggs(4, y=4)                        # self.calls is per-decoration here

"""
While useful for decorating functions, this coding scheme still has issues when applied
to methods—
"""
