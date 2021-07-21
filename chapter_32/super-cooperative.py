"Cooperative Multiple Inheritance Method Dispatch"
'The basics: Cooperative super call in action'

class B:
    def __init__(self): print('B.__init__')                                 # Disjoint class tree branches

class C:
    def __init__(self): print('C.__init__')

class D(B, C): pass


if __name__ == "__main__":
    x = D()                 # Runs leftmost only by default


class D(B, C):
    def __init__(self):                                             # Traditional form
        B.__init__(self)                                            # Invoke supers by name
        C.__init__(self)


if __name__ == "__main__":
    print()
    x = D()                 # Runs leftmost only by default


""" 
In diamond class tree patterns, though, explicit-name calls may by default trigger the
top-level class’s method more than once, though this might be subverted with additional
protocols (e.g., status markers in the instance):
""" 
class A:
    def __init__(self): print('A.__init__')

class B(A):
    def __init__(self): print('B.__init__'); A.__init__(self)

class C(A):
    def __init__(self): print('C.__init__'); A.__init__(self)    


if __name__ == "__main__":
    print()
    x = B()
    x = C()


class D(B, C): pass                                                 # Still runs leftmost only


if __name__ == "__main__":
    print()
    x = D()


class D(B, C):
    def __init__(self):                                             # Traditional form
        B.__init__(self)                                            # Invoke both supers by name
        C.__init__(self)


if __name__ == "__main__":
    print()
    x = D()                 # But this now invokes A twice!


"""
By contrast, if all classes use super, or are appropriately coerced by proxies to behave
as if they do, the method calls are dispatched according to class order in the MRO, such
that the top-level class’s method is run just once:
""" 
class A:
    def __init__(self): print('A.__init__')

class B(A):
    def __init__(self): print('B.__init__'); super().__init__()

class C(A):
    def __init__(self): print('C.__init__'); super().__init__()


if __name__ == "__main__":
    print()
    x = B()                 # Runs B.__init__, A is next super in self's B MRO
    x = C()                 # Runs C.__init__, A is next super in self's C MRO


class D(B, C): pass


if __name__ == "__main__":
    print()
    x = D()                 # Runs B.__init__, C is next super in self's D MRO!

    """ 
    The real magic behind this is the linear MRO list constructed for the class of self—
    because each class appears just once on this list, and because super dispatches to the
    next class on this list, it ensures an orderly invocation chain that visits each class just
    once. Crucially, the next class following B in the MRO differs depending on the class
    of self—it’s A for a B instance, but C for a D instance, accounting for the order of constructors
    run:
    """
    print()
    print(B.__mro__ )
    print(D.__mro__ )


'''
The MRO and its algorithm were presented earlier in this chapter. By selecting a next
class in the MRO sequence, a super call in a class’s method propagates the call through
the tree, so long as all classes do the same. In this mode super does not necessarily
choose a superclass at all; it picks the next in the linearized MRO, which might be a
sibling—or even a lower relative—in the class tree of a given instance.

Most Python programs do not rely on the nuances of
diamond pattern multiple inheritance trees. Super applies most directly to single
inheritance and cooperative diamond cases, and may seem superfluous for disjoint
nondiamond cases, where we might want to invoke superclass methods selectively or
independently. Even cooperative diamonds can be managed in other ways that may
afford programmers more control than an automatic MRO ordering can.
'''
