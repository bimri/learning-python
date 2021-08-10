"Coding Metaclasses"
# How, though, do we actually code a metaclass that customizes type?
'''
metaclasses are coded with
normal Python class statements and semantics. By definition, they are simply classes
that inherit from type. Their only substantial distinctions are that Python calls them
automatically at the end of a class statement, and that they must adhere to the interface
expected by the type superclass.
'''

'A Basic Metaclass'
'''
Perhaps the simplest metaclass you can code is simply a subclass of type with a
__new__ method that creates the class object by running the default version in type. A
metaclass __new__ like this is run by the __call__ method inherited from type; it typically
performs whatever customization is required and calls the type superclass’s
__new__ method to create and return the new class object:
'''
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # Run by inherited type.__call__
        return type.__new__(meta, classname, supers, classdict)


'''
This metaclass doesn’t really do anything (we might as well let the default type class
create the class), but it demonstrates the way a metaclass taps into the metaclass hook
to customize—because the metaclass is called at the end of a class statement, and
because the type object’s __call__ dispatches to the __new__ and __init__ methods,
code we provide in these methods can manage all the classes created from the metaclass.
'''

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    

class Eggs:
    pass


print('making class')
class Spam(Eggs, metaclass=MetaOne):                                # Inherits from Eggs, instance of MetaOne
    data = 1                                                        # Class data attribute
    def meth(self, arg):                                            # Class method attribute
        return self.data + arg
    

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


'metaclasses are for processing classes, and classes are for processing normal instances.'
