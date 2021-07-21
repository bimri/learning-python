"Basic super Usage and Its Tradeoffs"
'Odd semantics: A magic proxy in Python 3.X'
""" 
The super built-in actually has two intended roles. The more esoteric of these—cooperative
multiple inheritance dispatch protocols in diamond multiple-inheritance trees 

The role we’re interested in here is more commonly used, and more frequently requested
by people with Java backgrounds—to allow superclasses to be named generically
in inheritance trees. This is intended to promote simpler code maintenance, and to
avoid having to type long superclass reference paths in calls.
"""
class C:                                                            # In Python 3.X (only: see 2.X super form ahead)
    def act(self):
        print('spam')
    

class D(C):
    def act(self):
        super().act()                                               # Reference superclass generically, omit self
        print('eggs')

class E(C):
    def method(self):                                               # self is implicit in super...only!
        proxy = super()                                             # This form has no meaning outside a method
        print(proxy)                                                # Show the normally hidden proxy object
        proxy.act()                                                 # No arguments: implicitly calls superclass method!


if __name__ == '__main__':
    d = D()
    d.act()
    print(super)                                                    # A "magic" proxy object that routes later calls
    # super()                                                         # RuntimeError: super(): no arguments
    E().method()
