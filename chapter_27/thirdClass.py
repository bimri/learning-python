"A Third Example"
'''
    • __init__ is run when a new instance object is created: self is the new ThirdClass
    object.

    • __add__ is run when a ThirdClass instance appears in a + expression.

    • __str__ is run when an object is printed (technically, when it’s converted to its
    print string by the str built-in function or its Python internals equivalent).

'''
from secondClass import SecondClass


class ThirdClass(SecondClass):                              # Inherit from SecondClass
    def __init__(self, value):
        self.data = value                                   # On "ThirdClass(value)"

    def __add__(self, other):                               # On "self + other"
        return ThirdClass(self.data + other)
    
    def __str__(self):                                        # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):                                   # In-place change: named
        self.data *= other


"""
>>> a = ThirdClass('abc')                                   # __init__ called
>>> a.display()                                             # Inherited method called
Current value = "abc"

>>> print(a)                                                # __str__: returns display string
[ThirdClass: abc]
>>> b = a + 'xyz'                                           # __add__: makes a new instance
>>> b.display()                                             # b has all ThirdClass methods
Current value = "abcxyz"
>>> print(b)                                                # __str__: returns display string
[ThirdClass: abcxyz]

>>> a.mul(3)                                                # mul: changes instance in place
>>> print(a)
[ThirdClass: abcabcabc]
"""


'''
One overloading method we will use often here is the __init__ constructor method,
used to initialize newly created instance objects, and present in almost every realistic
class. Because it allows classes to fill out the attributes in their new instances immediately,
the constructor is useful for almost every kind of class you might code. In fact,
even though instance attributes are not declared in Python, you can usually find out
which attributes an instance will have by inspecting its class’s __init__ method.
'''
