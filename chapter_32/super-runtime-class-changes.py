"Runtime Class Changes and super"
'''
Superclass that might be changed at runtime dynamically preclude hardcoding their
names in a subclass’s methods, while super will happily look up the current superclass
dynamically. Still, this case may be too rare in practice to warrant the super model by
itself, and can often be implemented in other ways in the exceptional cases where it is
needed.
'''
class X:
    def m(self): print('X.m')

class Y:
    def m(self): print('Y.m')

class C(X):                                                         # Start out inheriting from X
    def m(self): super().m()                                        # Can't hardcode class name here


if __name__ == '__main__':
    print(C.__mro__)
    c = C()
    c.m()
    print(Y.__mro__)
    y = Y()
    y.m()

    C.__bases__ = (Y,)                                                  # Change superclass at runtime!
    c.m()


""" 
This works (and shares behavior-morphing goals with other deep magic, such as
changing an instance’s __class__), but seems rare in the extreme. Moreover, there may
be other ways to achieve the same effect—perhaps most simply, calling through the
current superclass tuple’s value indirectly: special code to be sure, but only for a very
special case (and perhaps not any more special than implicit routing by MROs):
""" 
class C(X):
    def m(self): C.__bases__[0].m(self)                                 # Special code for a special case


if __name__ == '__main__':
    print()
    i = C()
    i.m()

    C.__bases__ = (Y,)                                              # Same effect, without super()
    i.m()
