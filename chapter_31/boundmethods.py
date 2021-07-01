"Bound Methods and Other Callable Objects"
'''
bound methods can be processed as generic objects, just like
simple functions—they can be passed around a program arbitrarily

because bound methods combine both a function and an instance in a single package, they can
be treated like any other callable object and require no special syntax when invoked.
'''

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2 
    def triple(self):
        return self.base * 3
    

x = Number(2)                                               # Class instance objects
y = Number(3)                                               # State + methods
z = Number(4)
print(x.double())                                           # Normal immediate calls

acts = [x.double, y.double, y.triple, z.triple]             # List of bound methods
for act in acts:                                            # Calls are deferred
    print(act())                                            # Call as though functions


"""
Like simple functions, bound method objects have introspection information of their
own, including attributes that give access to the instance object and method function
they pair. Calling the bound method simply dispatches the pair:
"""
bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
print(bound())                                              # Calls bound.__func__(bound.__self__, ...)
