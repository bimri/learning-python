"Class Statement Protocol"
'''
Subclassing the type class to customize it is really only half of the magic behind metaclasses.
We still need to somehow route a class’s creation to the metaclass, instead of
the default type. To fully understand how this is arranged, we also need to know how
class statements do their business.
'''

""" 
We’ve already learned that when Python reaches a class statement, it runs its nested
block of code to create its attributes—all the names assigned at the top level of the
nested code block generate attributes in the resulting class object. These names are
usually method functions created by nested defs, but they can also be arbitrary attributes
assigned to create class data shared by all instances.

Technically speaking, Python follows a standard protocol to make this happen: at the
end of a class statement, and after running all its nested code in a namespace dictionary
corresponding to the class’s local scope, Python calls the type object to create the
class object like this:
"""

# class = type(classname, superclasses, attributedict)

"""
The type object in turn defines a __call__ operator overloading method that runs two
other methods when the type object is called:
"""

# type.__new__(typeclass, classname, superclasses, attributedict)
# type.__init__(class, classname, superclasses, attributedict)


'''
The __new__ method creates and returns the new class object, and then the __init__
method initializes the newly created object. As we’ll see in a moment, these are the
hooks that metaclass subclasses of type generally use to customize classes.
'''

class Eggs: ...                                     # Inherited names here

class Spam(Eggs):                                   # Inherits from Eggs
    data = 1                                            # Class data attribute
    def meth(self, arg):                            # Class method attribute
        return self.data + arg


"""
Python will internally run the nested code block to create two attributes of the class
(data and meth), and then call the type object to generate the class object at the end of
the class statement:
"""

# Spam = type('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})


'''
In fact, you can call type this way yourself to create a class dynamically—albeit here
with a fabricated method function and empty superclasses tuple (Python adds object
automatically in both 3.X and 2.X):
'''
x = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})
i = x()

print(x, i)
print(i.data, i.meth(2))


"The class produced is exactly like that you’d get from running a class statement:"
print(x.__bases__)

lc= [(a, v) for (a, v) in x.__dict__.items() if not a.startswith('__')]
print(lc)


""" 
Because this type call is made automatically at the end of the class statement, though,
it’s an ideal hook for augmenting or otherwise processing a class. The trick lies in
replacing the default type with a custom subclass that will intercept this call.
""" 
