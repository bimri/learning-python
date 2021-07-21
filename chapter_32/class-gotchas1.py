"Class Gotchas"
'Changing Mutable Class Attributes Can Have Side Effects, Too'

""" 
This gotcha is really an extension of the prior. Because class attributes are shared by all
instances, if a class attribute references a mutable object, changing that object in place
from any instance impacts all instances at once: 
""" 

if __name__ == "__main__":
    class C:
        shared = []                                                 # Class attribute
        def __init__(self):
            self.perobj = []                                        # Instance attribute
    
    x = C()                         # Two instances
    y = C()                         # Implicitly share class attrs
    print(y.shared, y.perobj)

    x.shared.append('spam')         # Impacts y's view too!
    x.perobj.append('spam')         # Impacts x's data only
    print(x.shared, x.perobj)

    print(y.shared, y.perobj)       # y sees change made through x
    print(C.shared)                 # Stored on class and shared


    """ 
    This effect is no different than many we’ve seen in this book already: mutable objects
    are shared by simple variables, globals are shared by functions, module-level objects
    are shared by multiple importers, and mutable function arguments are shared by the
    caller and the callee.
    """
    x.shared.append('spam')         # Changes shared object attached to class in place
    x.shared = 'spam'               # Changed or creates instance attribute attached to x
    