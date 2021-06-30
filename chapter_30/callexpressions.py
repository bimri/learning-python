"Call Expressions: __call__"
'''
the __call__ method is called when your instance
is called. Python runs a __call__ method
for function call expressions applied to your instances, 
passing along whatever positional or keyword arguments were sent.

This allows instances to conform to a functionbased
API:
'''
class Callee:
    def __call__(self, *pargs, **kargs):                             # Intercept instance calls
        print('Called:', pargs, kargs)                               # Accept arbitrary arguments
    

if __name__ == '__main__':
    C = Callee()
    C(1, 2, 3)                         # C is a callabnle object
    
    C(1, 2, 3, x=4, y=5)


"""
all the argument-passing modes are supported
by the __call__ method—whatever is passed to the instance is passed to this
method, along with the usual implied instance argument.

For example, the method definitions:
    class C:
        def __call__(self, a, b, c=5, d=6): ...                     # Normals and defaults
    class C:
        def __call__(self, *pargs, **kargs): ...                    # Collect arbitrary arguments
    class C:
        def __call__(self, *pargs, d=6, **kargs): ...               # 3.X keyword-only argument

all match all the following instance calls:
    X = C()
    X(1, 2)                                     # Omit defaults
    X(1, 2, 3, 4)                               # Positionals
    X(a=1, b=2, d=4)                            # Keywords
    X(*[1, 2], **dict(c=3, d=4))                # Unpack arbitrary arguments
    X(1, *(2,), c=3, **dict(d=4))               # Mixed modes


The net effect is that classes and
instances with a __call__ support the exact same argument syntax and semantics as
normal functions and methods.    

Intercepting call expression like this allows class instances to emulate the look and feel
of things like functions, but also retain state information for use during calls.
"""

class Prod:
    def __init__(self, value):                              # Accept just one argument
        self.value = value
    def __call__(self, other):
        return self.value * other 


if __name__ == '__main__':
    print()
    x = Prod(2)
    print(x(3))
    print(x(4))



"""
However, __call__ can become more useful when interfacing with APIs (i.e., libraries)
that expect functions—it allows us to code objects that conform to an expected function
call interface, but also retain state information, and other class assets such as inheritance.
In fact, it may be the third most commonly used operator overloading
method, behind the __init__ constructor and the __str__ and __repr__ display-format
alternatives.
"""
