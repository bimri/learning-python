class Methods:
    def imeth(self, x):                                 # Normal instance method: passed a self
        print([self, x])
    
    def smeth(x):                                       # Static: no instance passed
        print([x]) 
    
    def cmeth(cls, x):                                  # Class: gets class, not instance 
        print([cls, x]) 
    
    smeth = staticmethod(smeth)                         # Make smeth a static method(or @: ahead)
    cmeth = classmethod(cmeth)                          # Make cmeth a class method (or @: ahead)

'''
Notice how the last two assignments in this code simply reassign (a.k.a. rebind) the
method names smeth and cmeth. Attributes are created and changed by any assignment
in a class statement, so these final assignments simply overwrite the assignments made
earlier by the defs.

Python now supports three kinds of class-related methods, with differing
argument protocols:
    • Instance methods, passed a self instance object (the default)
    • Static methods, passed no extra object (via staticmethod)
    • Class methods, passed a class object (via classmethod, and inherent in metaclasses)

# An instance method must always be called with an instance object.
'''


if __name__ == "__main__":
    from bothmethods import Methods             # Normal instance method: passed a self
    obj = Methods()                             # Callable through instance or class
    obj.imeth(1)                            
    Methods.imeth(obj, 2)
    
    """ 
    Static methods, by contrast, are called without an instance argument. Unlike simple
    functions outside a class, their names are local to the scopes of the classes in which they
    are defined, and they may be looked up by inheritance. Instance-less functions can be
    called through a class normally in Python 3.X
    Using the staticmethod built-in allows such methods to also be called through an instance in 3.X
    """
    Methods.smeth(3)                            # Static method: call through class
                                                # No instance passed or expected
    obj.smeth(4)                                # Static method: call through instance
                                                # Instance not passed

    """
    Class methods are similar, but Python automatically passes the class (not an instance)
    in to a class method’s first (leftmost) argument, whether it is called through a class or
    an instance:
    """ 
    Methods.cmeth(5)                             # Class method: call through class
                                                 # Becomes cmeth(Methods, 5)
    obj.cmeth(6)                                 # Class method: call through instance
                                                 # Becomes cmeth(obj, 6)
