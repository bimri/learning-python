"How Properties and Descriptors Relate"
'''
properties and descriptors are strongly related—the property
built-in is just a convenient way to create a descriptor.
'''
class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel                                            # Save unbound methods
        self.__doc__ = doc                                          # or other callables
    
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)                                  # Pass instancce to self
                                                                    # in property accessors

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)
    
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)
    

class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)                           # Use like property()


x = Person()
x.name 
x.name = 'Bob'
del x.name 


'''
This Property class catches attribute accesses with the descriptor protocol and routes
requests to functions or methods passed in and saved in descriptor state when the class
is created. Attribute fetches, for example, are routed from the Person class, to the
Property class’s __get__ method, and back to the Person class’s getName. With descriptors,
this “just works”:

Note that this descriptor class equivalent only handles basic property usage, though;
to use @ decorator syntax to also specify set and delete operations, we’d have to extend
our Property class with setter and deleter methods, which would save the decorated
accessor function and return the property object (self should suffice). Since the prop
erty built-in already does this.
'''
