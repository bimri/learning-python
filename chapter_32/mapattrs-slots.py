# class-based slots
# test __slots__ attribute inheritance 
from mapattrs import mapattrs, trace 

class A(object):
    __slots__ = ['a', 'b'] 
    x = 1
    y = 2

class B(A):
    __slots__ = ['b', 'c']

class C(A):       x = 2

class D(B, C):
    z = 3 
    def __init__(self):
        self.name = 'bimri'
    

I = D()
print(I.name)
# print(trace(mapattrs, bysource=True))           # Also: trace(mapattrs(i))
