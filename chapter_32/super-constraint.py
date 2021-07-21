"Constraint: Call chain anchor requirement"
'''
The super call comes with complexities that may not be apparent on first encounter,
and may even seem initially like features. the MRO ordering
can be used even in cases where the diamond is only implicit—in the following, triggering
constructors in independent classes automatically:
'''
class B:
    def __init__(self): print('B.__init__'); super().__init__()

class C:
    def __init__(self): print('C.__init__'); super().__init__()


if __name__ == "__main__":
    x = B()                                                         # object is an implied super at the end of MRO
    x = C()


class D(B, C): pass                                                 # Inherits B.__init__ but B's MRO differs for D


if __name__ == "__main__":
    print()
    x = D()                     # Runs B.__init__, C is next super in self's D MRO!

    """ 
    Technically, this dispatch model generally requires that the method being called by
    super must exist, and must have the same argument signature across the class tree, and
    every appearance of the method but the last must use super itself. This prior example
    works only because the implied object superclass at the end of the MRO of all three
    classes happens to have a compatible __init__ that satisfies these rules:
    """
    print()
    print(B.__mro__)
    print(D.__mro__)


""" 
By contrast, in such cases direct calls incur neither extra coding requirements nor added
performance cost, and make dispatch more explicit and direct:
"""
class B:
    def __init__(self): print('B.__init__')

class C:
    def __init__(self): print('C.__init__') 

class D(B, C):
    def __init__(self): B.__init__(self); C.__init__(self)   


if __name__ == "__main__":
    print()
    print()
    x = D()
    