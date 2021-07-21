"A First Look at User-Defined Function Decorators"
'''
Because the spam function is run through the tracer decorator, when the original
spam name is called it actually triggers the __call__ method in the class. This method
counts and logs the call, and then dispatches it to the original wrapped function.
'''

class tracer:
    def __init__(self, func):                                           # Remember original, init counter
        self.calls = 0
        self.func = func
    def __call__(self, *args):                                          # On later calls: add logic, run original
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)


"The net effect is to add a layer of logic to the original spam function."
@tracer                                                                 # Same as spam = tracer(spam)
def spam(a, b, c):                                                      # Wrap spam in a decorator object
    return a + b + c

print(spam(1, 2, 3))                                                    # Really calls the tracer wrapper object
print(spam('a', 'b', 'c'))                                              # Invokes __call__ in class
