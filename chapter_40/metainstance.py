class MetaOne(type):
    def __new__(meta, classname, supers, classdict):                # Redefine type method
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        return 'toast'


class Super(metaclass=MetaOne):                                     # Metaclass inherited by subs too
    def spam(self):                                                 # MetaOne run twice for two classes
        return 'spam'
    class Sub(Super):                                               # Superclass: inheritance versus instance
        def eggs(self):                                             # Classes inherit from super
            return 'eggs'                                           # But not from metaclasses


"""
When this code is run (as a script or module), the metaclass handles construction of
both client classes, and instances inherit class attributes but not metaclass attributes:
    >>> from metainstance import * # Runs class statements: metaclass run twice
    In MetaOne.new: Super
    In MetaOne.new: Sub
    >>> X = Sub() # Normal instance of user-defined class
    >>> X.eggs() # Inherited from Sub
    'eggs'
    >>> X.spam() # Inherited from Super
    'spam'
    >>> X.toast() # Not inherited from metaclass
    AttributeError: 'Sub' object has no attribute 'toast'

By contrast, classes both inherit names from their superclasses, and acquire names from
their metaclass (which in this example is itself inherited from a superclass):
    >>> Sub.eggs(X) # Own method
    'eggs'
    >>> Sub.spam(X) # Inherited from Super
    'spam'
    >>> Sub.toast() # Acquired from metaclass
    'toast'
    >>> Sub.toast(X) # Not a normal class method
    TypeError: toast() takes 1 positional argument but 2 were given

Notice how the last of the preceding calls fails when we pass in an instance, because
the name resolves to a metaclass method, not a normal class method. In fact, both the
object you fetch a name from and its source become crucial here. Methods acquired
from metaclasses are bound to the subject class, while methods from normal classes
are unbound if fetched through the class but bound when fetched through the instance:
    >>> Sub.toast
    <bound method MetaOne.toast of <class 'metainstance.Sub'>>
    >>> Sub.spam
    <function Super.spam at 0x0298A2F0>
    >>> X.spam
    <bound method Sub.spam of <metainstance.Sub object at 0x02987438>>
"""
