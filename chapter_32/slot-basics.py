"Slots: Attribute Declarations"
'''
slots should be used only in applications that clearly warrant the added
complexity. They will complicate your code, may complicate or break code you may
use, and require universal deployment to be effective
'''
"Slot basics"
# To use slots, assign a sequence of string names to the special __slots__ variable &
# attribute at the top od a class statement only thise names in the __slots__ list can 
# be assigned as instance attributes. (instance names must be assigned before they can 
# be referenced)
class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
'must assign before use'
# x.age = 42 # AttributeError: 'limiter' object has no attribute 'age'  

x.age = 40                                          # Looks like instance data 
print(x.age)

# x.ape = 1000                                      # "Illegal: not in __slots__" AttributeError: 'limiter' object has no attribute 'ape'


"Slots and namespace dictionaries"
class C:
    __slots__ = ['a', 'b']                          # __slots__ means no __dict__ by default

X = C()
X.a = 1
print(X.a)

# AttributeError: 'C' object has no attribute '__dict__'
# print(X.__dict__)

'''
However, we can still fetch and set slot-based attributes by name string using storageneutral
tools such as getattr and setattr (which look beyond the instance __dict__
and thus include class-level names like slots) and dir (which collects all inherited names
throughout a class tree):
'''
print(getattr(X, 'a'))
setattr(X, 'b', 2)                                   # But getattr() and setattr() still work
print(X.b)

print('a' in dir(X))                                 # And dir() finds slot attributes too
print('b' in dir(X))


'''
Also keep in mind that without an attribute namespace dictionary, it’s not possible to
assign new names to instances that are not names in the slots list:
'''
class D:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 3                                  # Cannot add new names if no __dict__
    
# AttributeError: 'D' object has no attribute 'c'
# X = D()


'''
We can still accommodate extra attributes, though, by including __dict__ explicitly in
__slots__, in order to create an attribute namespace dictionary too:
'''
class D:
    __slots__ = ['a', 'b', "__dict__"]              # Name __dict__ to include one too
    c = 3 
    def __init__(self):
        self.d = 4                                  # d stores in __dict__, a is a slot

    
X = D()
print(X.d)
print(X.c)

# All instance attrs undefined until assigned
# print(X.a)
X.a = 1
X.b = 2 

'''
In this case, both storage mechanisms are used. This renders __dict__ too limited for
code that wishes to treat slots as instance data, but generic tools such as getattr still
allow us to process both storage forms as a single set of attributes:
'''
print(X.__dict__)                                   # Some objects have both __dict__ and slot names
print(X.__slots__)                                  # getattr() can fetch either type of attr 

# Fetch all three forms 
print(
    getattr(X, 'a'),
    getattr(X, 'c'),
    getattr(X, 'd')
)    

# list just instance attributes 
for attr in list(X.__dict__) + X.__slots__:
    print(attr, '=>', getattr(X, attr))


"Multiple __slot__ in superclasses"
'''
Specifically, this code addresses only slot names in the lowest __slots__ attribute
inherited by an instance, but slot lists may appear more than once in a class tree. That
is, a name’s absence in the lowest __slots__ list does not preclude its existence in a
higher __slots__. Because slot names become class-level attributes, instances acquire
the union of all slot names anywhere in the tree, by the normal inheritance rule:
'''
class E:
    __slots__ = ['c', 'd']                                      # Superclass has slots
class D(E):
    __slots__ = ['a', '__dict__']                               # But so does its subclass

X = D()
X.a = 1; X.b = 2; X.c = 3                                       # The instance is the union(slots: a, c)
print(X.a, X.c)

"Inspecting just the inherited slots list won’t pick up slots defined higher in a class tree:"
print(E.__slots__)                                                     # But slots are not concatenated
print(D.__slots__)                                                     
print(X.__slots__)                                                     # Instance inherits "lowest" __slots__
print(X.__dict__)                                                      # And has its own an attr dict

for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

print(dir(X))
