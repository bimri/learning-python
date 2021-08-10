"Metaclass Methods"
'''
Just as important as the inheritance of names, methods in metaclasses process their
instance classes—not the normal instance objects we’ve known as “self,” but classes
themselves.

They again are available in the metaclasses instance realm only,
not to normal instance inheritance. The failure at the end of the following, for example,
stems from the explicit name inheritance rules of the prior section:
'''
class A(type):
    def x(cls): print('ax', cls)                            # A metaclass (instances=classes)
    def y(cls): print('ay', cls)                            # y is overridden by instance B    


class B(metaclass=A):
    def y(self): print('by', self)                          # A normal class (normal instances)
    def z(self): print('bz', self)                          # Namespace dict holds y and z


B.x                     # x acquired from metaclass
B.y                     # y and z defined in class itself
B.z
B.x()                   # Metaclass method call: gets cls


I = B()                 # Instance method calls: get inst
I.y()
I.z()
I.x()                   # Instance doesn't see meta names
