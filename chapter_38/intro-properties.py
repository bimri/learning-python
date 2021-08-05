"Properties"
'''
The property protocol allows us to route a specific attribute’s get, set, and delete operations
to functions or methods we provide, enabling us to insert code to be run automatically
on attribute access, intercept attribute deletions, and provide documentation
for the attributes if desired.

Properties are created with the property built-in and are assigned to class attributes,
just like method functions. Accordingly, they are inherited by subclasses and instances,
like any other class attributes. Their access-interception functions are provided with
the self instance argument, which grants access to state information and class attributes
available on the subject instance.

A property manages a single, specific attribute; although it can’t catch all attribute
accesses generically, it allows us to control both fetch and assignment accesses and
enables us to change an attribute from simple data to a computation freely, without
breaking existing code.
'''


'The Basics'
"A property is created by assigning the result of a built-in function to a class attribute:"
# None of this built-in’s arguments are required, 
# and all default to None if not passed.
"""
For the first three, this None means that the corresponding operation is not supported, and
attempting it will raise an AttributeError exception automatically.
"""
# attribute = property(fget, fset, fdel, doc)


'A First Example'
class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

bimri = Person('Bimri Codes')               # bimri has a managed attribute
print(bimri.name)                           # Runs getName

bimri.name = 'Codes Bimri'                  # Runs setName
print(bimri.name)

del bimri.name                              # Runs delName

print('-'*20)
cassandra = Person('Cassandra Codes')       # cassandra inherits property too
print(cassandra.name)
print(Person.name.__doc__)                  # Or help(Person.name)
