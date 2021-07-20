"""
programs can be more inclusive by relying on dir to
fetch all inherited attribute names and getattr to fetch their corresponding values for
the instance—without regard to their physical location or implementation. If you must
support slots as instance data, this is likely the most robust way to proceed
"""
class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data 
    

I = Slotful(10)
I.a, I.b = 10, 20
print(
    # Normal attribute fetch
    I.a, 
    I.b,
    I.c
)

# Both __dict__ and slots storage 
print( 
    [x for x in dir(I) if not x.startswith('__')]
)

print(I.__dict__['c'])                                      # __dict__ is only one attr source

print(
    getattr(I, 'c'),                                            # dir+getattr is broader than __dict__
    getattr(I, 'a'),                                            # applies to slots, properties, descrip
)

for a in (x for x in dir(I) if not x.startswith('__')):
    print(a, getattr(I, a))



"Slot usage rules"
class C: pass                                                   # Bullet 1: slots in sub but not super 
class D(C): __slots__ = ["a"]                                   # Makes instance dict for nonslots 
X = D()
X.a = 1; X.b = 2 
print(X.__dict__) 
print(D.__dict__.keys())

class C: __slots__ = ["a"]                                     # Bullet 2: slots in super but not sub
class D(C): pass                                               # Makes instance dict for nonslots
X = D()                                                        # But slot name still managed in class 
X.a = 1; X.b = 2
print(X.__dict__) 
print(C.__dict__.keys())

class C: __slots__ = ["a"]                                      # Bullet 3: only lowest slot accessible 
class D(C): __slots__ = ["a"]                                  

# ValueError: 'a' is not a valid slot name
# class C: __slots__ = ['a']; a = 99                              # Bullet 4: no class-level defaults

""" 
besides their program-breaking potential, slots essentially require both
universal and careful deployment to be effective—because slots do not compute values
dynamically like properties, they are largely pointless
unless each class in a tree uses them and is cautious to define only new slot names not
defined by other classes. It’s an all-or-nothing feature— 
"""
class C: __slots__ = ['a']                                       # Assumes universal use, different names 
class D(C): __slots__ = ['b']                                    # Assumes careful deployment, same names
X = D()
X.a = 1; X.b = 2

# AttributeError: 'D' object has no attribute '__dict__'
# print(X.__dict__)

print(C.__dict__.keys()); print(D.__dict__.keys())
