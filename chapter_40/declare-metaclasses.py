"Declaring Metaclasses"
'''
classes are created by the type class by default. To tell Python to
create a class with a custom metaclass instead, you simply need to declare a metaclass
to intercept the normal instance creation call in a user-defined class.
'''
"desired metaclass as a keyword argument in the class header"
class Spam(metaclass=Meta): ...


'''
Inheritance superclasses can be listed in the header as well. In the following, for example,
the new class Spam inherits from superclass Eggs, but is also an instance of and
is created by metaclass Meta:
'''
class Spam(Eggs, metaclass=Meta): ...                      # Normal supers OK: must list first


'''
In this form, superclasses must be listed before the metaclass; in effect, the ordering
rules used for keyword arguments in function calls apply here.
'''
