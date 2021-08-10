"Metaclass Dispatch in Both 3.X and 2.X"
'''
When a specific metaclass is declared per the prior sections’ syntax, the call to create
the class object run at the end of the class statement is modified to invoke the metaclass
instead of the type default:
'''
# class = Meta(classname, superclasses, attributedict)

'''
And because the metaclass is a subclass of type, the type class’s __call__ delegates the
calls to create and initialize the new class object to the metaclass, if it defines custom
versions of these methods:
'''
# Meta.__new__(Meta, classname, superclasses, attributedict)
# Meta.__init__(class, classname, superclasses, attributedict)


"""
To demonstrate, here’s the prior section’s example again, augmented with a 3.X metaclass
specification:
"""

class Spam(Eggs, metaclass=Meta):                       # Inherits from Eggs, instance of Meta
    data = 1                                            # Class data attribute
    def meth(self, arg):                                # Class method attribute
        return self.data + arg


"""
At the end of this class statement, Python internally runs the following to create the
class object—again, a call you could make manually too, but automatically run by
Python’s class machinery:
"""
# Spam = Meta('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})


"""
If the metaclass defines its own versions of __new__ or __init__, they will be invoked
in turn during this call by the inherited type class’s __call__ method, to create and
initialize the new class. The net effect is to automatically run methods the metaclass
provides, as part of the class construction process.
"""
