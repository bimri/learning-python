"Descriptors"
'A First Example'
'''
The following defines a descriptor that intercepts
access to an attribute named name in its clients. Its methods use their instance argument
to access state information in the subject instance, where the name string is actually
stored.
'''
class Name:
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value 
    def __delete__(self, instance):
        print('remove')
        del instance._name
    
class Person:
    def __init__(self, name):
        self._name = name
    name = Name()                                   # Assign descriptor to attr


bob = Person('Bob Smith')                           # bob has a managed attribute
print(bob.name)                                     # Runs Name.__get__
bob.name = 'Robert Smith'                           # Runs Name.__set__
print(bob.name)
del bob.name                                        # Runs Name.__delete__

print('-'*20)
sue = Person('Sue Jones')                           # sue inherits descriptor too
print(sue.name)
print(Name.__doc__)                                 # Or help(Name)


"""
Notice in this code how we assign an instance of our descriptor class to a class attribute
in the client class; because of this, it is inherited by all instances of the class, just
like a class’s methods. Really, we must assign the descriptor to a class attribute like this
—it won’t work if assigned to a self instance attribute instead. When the descriptor’s
__get__ method is run, it is passed three objects to define its context:
    • self is the Name class instance.
    • instance is the Person class instance.
    • owner is the Person class.
"""

"""
Also note that when a descriptor class is not useful outside the client class, it’s perfectly
reasonable to embed the descriptor’s definition inside its client syntactically. Here’s
what our example looks like if we use a nested class:
"""
class Person:
    def __init__(self, name):
        self._name = name
    
    class Name:                                     # Using a nested class
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()
