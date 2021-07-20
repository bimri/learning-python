# from .. import ListTree

class C(ListTree): pass 
X = C()                                                 # OK: no __slots__ used 
print(X) 

class C(ListTree): __slots__ = ['a', 'b']               # OK: superclass produces __dict__
X = C()                                                 # OK: __slots__ used
X.c = 3
print(X)                                                # Displays c at X, a and b at C 

"""
The following classes display correctly as well—any nonslot class like ListTree generates
an instance __dict__, and can thus safely assume its presence:
"""
class A: __slots__ = ['a']                              # Both OK by default 1 above 
class B(A, ListTree): pass

class A: __slots__ = ['a']                              
class B(A, ListTree): __slots__ = ['b']                 # Displays b at B, a at A

