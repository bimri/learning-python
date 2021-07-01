"Unbound Methods Are Functions in 3.X"  
'''
In Python 3.X, the language has dropped the notion of unbound methods. What we
describe as an unbound method here is treated as a simple function in 3.X.
'''
class Selfless:
    def __init__(self, data):
        self.data = data 
    def selfless(arg1, arg2):                               # A simple function in 3.X
        return arg1 + arg2
    def normal(self, arg1, arg2):                           # Instance expected when called
        return self.data + arg1 + arg2 
    

X = Selfless(2)

x = X.normal(3, 4)                                              # Instance passed to self automatically: 2+(3+4)
print(x)

y = Selfless.normal(X, 3, 4)                                    # self expected by method: pass manually
print(y)

z = Selfless.selfless(3, 4)                                     # No instance: works in 3.X, fails in 2.X
print(z)


'''
Although this removes some potential error trapping in 3.X
(what if a programmer accidentally forgets to pass an instance?), it allows a class’s
methods to be used as simple functions as long as they are not passed and do not expect
a “self” instance argument.
'''

"""
The following two calls still fail in both 3.X and 2.X, though—the first (calling through
an instance) automatically passes an instance to a method that does not expect one,
while the second (calling through a class) does not pass an instance to a method that
does expect one (error message text here is per 3.3):
    >>> X.selfless(3, 4)
    TypeError: selfless() takes 2 positional arguments but 3 were given

    >>> Selfless.normal(3, 4)
    TypeError: normal() missing 1 required positional argument: 'arg2'

Because of this change, the staticmethod built-in function and decorator described in
the next chapter is not needed in 3.X for methods without a self argument that are
called only through the class name, and never through an instance—such methods are
run as simple functions, without receiving an instance argument.
"""
