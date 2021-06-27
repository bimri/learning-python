class Super:
    def hello(self):
        self.data1 = 'spam'
    
class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'
    

X = Sub()
print(
    X.__dict__                                          # Instance namespace dict
)                                       

print(
    X.__class__                                         # Class of intance
)

print(
    Sub.__bases__                                       # Superclasses of class
)

print(
    Super.__bases__                                     # () empty tuple in Python 2.X
)


'''
As classes assign to self attributes, they populate the instance objects—that is, attributes
wind up in the instances’ attribute namespace dictionaries, not in the classes’.
An instance object’s namespace records data that can vary from instance to instance,
and self is a hook into that namespace:'''
Y = Sub()
X.hello()
print(X.__dict__)

X.hola()
print(X.__dict__)

print(list(Sub.__dict__.keys()))
print(list(Super.__dict__.keys()))

print(Y.__dict__)


'''
each instance has an independent namespace dictionary,
which starts out empty and can record completely different attributes than those
recorded by the namespace dictionaries of other instances of the same class.
'''

"""
Because attributes are actually dictionary keys inside Python, there are really two ways
to fetch and assign their values—by qualification, or by key indexing:
"""
print(
    X.data1, X.__dict__['data1']
)

X.data3 = 'toast'
print(X.__dict__)

X.__dict__['data3'] = 'ham'
print(X.data3)

# This equivalence applies only to attributes actually attached to the instance
# Because attribute fetch qualification also performs an inheritance search, it can access
# inherited attributes that namespace dictionary indexing cannot.
"The inherited attribute X.hello, for instance, cannot be accessed by X.__dict__['hello']."

'try running these objects through the dir function'
'''
dir(X) is similar to
X.__dict__.keys(), but dir sorts its list and includes some inherited and built-in attributes.
'''