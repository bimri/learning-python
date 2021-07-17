"Diamond Inheritance Change"
'Implications for diamond inheritance trees'

class A:        attr = 1                                # New-style class("object" not requires in 3.X)
class B(A):     pass                                    
class C(A):     attr = 2                                # C only changes attr
class D(B, C):  pass                                    # Tries C before A

x = D()
print(x.attr)                                           # Searches x, then D, then B, then C


'Explicit conflict resolution'
class A(object): attr = 1                               # New-style 
class B(A):      pass 
class C(A):      attr = 2                               # C changes attr
class D(B, C):   attr = B.attr                          # D <== Choose A.attr, above

y = D
print(y.attr)                                           # Prints 1, as D has A.attr


class A:
    def meth(self): print('A.meth')

class C(A):
    def meth(self): print('C.meth')

class B(A):
    pass

class D(B, C): pass                                     # Use defaults search order
x = D()                                                 # Will vary per class type 
x.meth()                                         # Defaults to classic order in 2.x

class D(B, C): meth = C.meth                            # Override C.meth   
x = D()                                                 # Will vary per class type
x.meth()                                                # Prints C.meth, as per new-style

class D(B, C): meth = B.meth                            # <== Pick B.meth, above
x = D()                                                 # Will vary per class type
x.meth()                                                # Prints B.meth, as per new-style


"More on the MRO: Method Resolution Order"
'''
Tracing the MRO
If you just want to see how Python’s new-style inheritance orders superclasses in general,
though, new-style classes (and hence all classes in 3.X) have a class.__mro__ attribute,
which is a tuple giving the linear search order Python uses to look up attributes
in superclasses. Really, this attribute is the inheritance order in new-style classes, and
is often as much MRO detail as many Python users need.
'''
class A: pass 
class B(A): pass                                        # Diamonds: order differs for newstyle
class C(A): pass                                        # Breadth-first across lower levels
class D(B, C): pass             

print(D.__mro__)
print(A.__bases__)                                      # Superclass links: object at two roots
print(B.__bases__)
print(C.__bases__)
print(D.__bases__)

"The MRO of a class is a tuple of its superclasses, ordered by the order in which they appear in the class definition."


class X: pass 
class Y: pass 
class A(X): pass                                        # Nondiamond: depth first then left to right
class B(Y): pass                                        # Though implied "object" always forms a diamond
class D(A, B): pass         

print(D.mro())                                           # Prints the MRO of D

print(X.__bases__, Y.__bases__)
print(A.__bases__, B.__bases__)


"""
Strictly speaking, new-style classes also have a
class.mro() method used in the prior example for variety; it’s called at class instantiation
time and its return value is a list used to initialize the __mro__ attribute when the
class is created
"""
print(
    D.mro() == list(D.__mro__)                         # Prints True    
)
print([cls.__name__ for cls in D.__mro__])
