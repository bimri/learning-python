"Listing inherited attributes with dir"

"""
Generic lister mixin tester: similar to transitive reloader in
Chapter 25, but passes a class object to tester (not funciton),
and testByNames adds loading of both module and class by name
strings here, in keeping with chapter 31's factories pattern.
"""
import importlib 

def tester(listerclass, sept=False):

    class Super:
        def __init__(self):                                 # Superclass __init__
            self.data1 = 'spam'                             # Create instance attrs
        def ham(self):
            pass
    
    class Sub(Super, listerclass):                          # Mix in ham and a __str__
        def __init__(self):                                 # Listers have access to self
            Super.__init__(self)
            self.data2 = 'eggs'                             # More instance attrs
            self.data3 = 42                 
        def spam(self):
            pass

    instance = Sub()                                      # Return instance with lister's __str__
    print(instance)                                         # Run mixed-in __str__(or via str(x))
    if sept: print("-" * 80)

def testByNames(modname, classname, sept=False):
    modobject   = importlib.import_module(modname)          # Import by namestring
    listerclass = getattr(modobject, classname)             # Fetch attr by namestring 
    tester(listerclass, sept)


if __name__ == '__main__':
    testByNames('listinstance',  'ListInstance',  True)       # Test all three here 
    # testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree',      'ListTree',      False)


"""
While it’s at it, this script also adds the ability to specify test module and class by name
string, and leverages this in its self-test code—an application of the factory pattern’s
mechanics described earlier.
# mix-in classes are the class equivalent of modules—packages of
# methods useful in a variety of clients
    >>> import listinstance
    >>> class C(listinstance.ListInstance): pass
    
    >>> x = C()
    >>> x.a, x.b, x.c = 1, 2, 3
    >>> print(x)
    <Instance of C, address 43230824:
    a=1
    b=2
    c=3
    >
Besides the utility they provide, mix-ins optimize code maintenance, like all classes do.
"""
