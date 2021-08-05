"Coding Properties with Decorators"
'''
Recall that the function decorator syntax:
    @decorator
    def func(args): ...
is automatically translated to this equivalent by Python, to rebind the function name
to the result of the decorator callable:
    def func(args): ...
    func = decorator(func)    
Because of this mapping, it turns out that the property built-in can serve as a decorator,
to define a function that will run automatically when an attribute is fetched:
    class Person:
        @property
        def name(self): ... # Rebinds: name = property(name)
When run, the decorated method is automatically passed to the first argument of the
property built-in. This is really just alternative syntax for creating a property and rebinding
the attribute name manually, but may be seen as more explicit in this role:
    class Person:
        def name(self): ...
        name = property(name)
'''

'Setter and deleter decorators'
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):                         # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name
    
    @name.setter
    def name(self, value):                  # name = name.setter(name)
        print('change...')
        self._name = value
    
    @name.deleter
    def name(self):                         # name = name.deleter(name)
        print('remove...')
        del self._name

bob = Person('Bob Smith')                   # bob has a managed attribute
print(bob.name)                             # Runs name getter (name 1)
bob.name = 'Robert Smith'                   # Runs name setter (name 2)
print(bob.name)
del bob.name                                # Runs name deleter (name 3)

print('-'*20)
sue = Person('Sue Jones')                   # sue inherits property too
print(sue.name)
print(Person.name.__doc__)                  # Or help(Person.name)
