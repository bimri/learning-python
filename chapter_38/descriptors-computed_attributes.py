"Computed Attributes"

class DescSquare:
    def __init__(self, start):                          # Each desc has own state
        self.value = start
    def __get__(self, instance, owner):                 # On attr fetch
        return self.value ** 2
    def __set__(self, instance, value):                 # On attr assign
        self.value = value                              # No delete or docs

class Client1:
    X = DescSquare(3)                                   # Assign descriptor instance to class attr

class Client2:
    X = DescSquare(32)                                  # Another instance in another client class
                                                        # Could also code two instances in same class

c1 = Client1()
c2 = Client2()

print(c1.X)                                             # 3 ** 2
c1.X = 4
print(c1.X)                                             # 4 ** 2
print(c2.X)                                             # 32 ** 2 (1024)


'Using State Information in Descriptors'
'''
Descriptors can use both instance state and descriptor state, or any combination thereof:
    • Descriptor state is used to manage either data internal to the workings of the descriptor,
    or data that spans all instances. It can vary per attribute appearance (often,
    per client class).
    • Instance state records information related to and possibly created by the client class.
    It can vary per client class instance (that is, per application object).

descriptor state is per-descriptor data and instance state is per-clientinstance data.    
'''
class DescState:
    def __init__(self, value):                          
        self.value = value
    def __get__(self, instance, owner):                             # On attr fetch     
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):                             # On attr assign     
        print('DescState set')
        self.value = value
    

# Client class
class CalcAttrs:
    X = DescState(2)                                                # Descriptor class attr
    Y = 3                                                           # Class attr
    def __init__(self):
        self.Z = 4                                                  # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                                          # X is computed, others are not
obj.X = 5                                                           # X assignment is intercepted
CalcAttrs.Y = 6                                                     # Y reassigned in class
obj.Z = 7                                                           # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                                                  # But X uses shared data, like Y!
print(obj2.X, obj2.Y, obj2.Z)


"""
It’s also feasible for a descriptor to store or use an attribute attached to the client class’s
instance, instead of itself. Crucially, unlike data stored in the descriptor itself, this allows
for data that can vary per client class instance. 
"""
class InstState:    
    def __get__(self, instance, owner):
        print('InstState get')                          # Assume set by client class
        return instance._X * 10 
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value 


# Client class
class CalcAttrs:
    X = InstState()                                     # Descriptor class attr
    Y = 3
    def __init__(self):
        self._X = 2                                     # Instance attr
        self.Z  = 4                                     # Instance attr


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                              # X is computed, others are not
obj.X = 5
CalcAttrs.Y = 6                                         # X assigned is intercepted
obj.Z = 7                                               # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()
print(obj2.X, obj2.Y, obj2.Z)


class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)
    def __set__(self, instance, value):
        instance.data = value 
    
class Client:
    def __init__(self, data):
        self.data = data
    managed = DescBoth('spam')

I = Client('eggs')
print(I.managed)

I.managed = 'SPAM'                                      # Change instance data
print(I.managed)



"""
Whether you should
access these this way probably varies per program—properties and descriptors may
run arbitrary computation, and may be less obviously instance “data” than slots:
"""
print(I.__dict__)
print(
    [x for x in dir(I) if not x.startswith('__')]
)

print(getattr(I, 'data'))
print(getattr(I, 'managed'))

for attr in (x for x in dir(I) if not x.startswith('__')):
    print('%s => %s' % (attr, getattr(I, attr)))
