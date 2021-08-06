"Intercepting Built-in Operation Attributes"

class GetAttr:
    eggs = 88                                                   # eggs stored on class, spam on instance
    def __init__(self):
        self.spam = 77
    
    def __len__(self):                                          # len here, else __getattr__ called with __len__
        print('__len__: 42')
        return 42
    
    def __getattr__(self, attr):                                # Provide __str__ if asked, else dummy func
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute(object):                                     # object required in 2.X, implied in 3.X
    eggs = 88                                                   # In 2.X all are isinstance(object) auto
    def __init__(self):                                         # But must derive to get new-style tools,
        self.spam = 77                                          # incl __getattribute__, some __X__ defaults
    
    def __len__(self):
        print('__len__: 42')
        return 42
    
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))


X = Class()
X.eggs                          # Class attr
X.spam                          # Instance attr
X.other                         # Missing attr
len(X)                          # __len__ defined explicitly


# New-styles must support [], +, call directly: redefine

try: X[0]                                                       # __getitem__?
except: print('fail []')

try: X + 99                                                     # __add__?
except: print('fail +')

try: X()                                                        # __call__? (implicit via built-in)
except: print('fail ()')

X.__call__()                                                    # __call__? (explicit, not inherited)
print(X.__str__())                                              # __str__? (explicit, inherited from type)
print(X)                                                        # __str__? (implicit via built-in)


""" 
Trace these outputs back to prints in the script to see how this works. Some highlights:
    • __str__ access fails to be caught twice by __getattr__ in 3.X: once for the built-in
    print, and once for explicit fetches because a default is inherited from the class
    (really, from the built-in object, which is an automatic superclass to every class in
    3.X).
    
    • __str__ fails to be caught only once by the __getattribute__ catchall, during the
    built-in print operation; explicit fetches bypass the inherited version.
    
    • __call__ fails to be caught in both schemes in 3.X for built-in call expressions, but
    it is intercepted by both when fetched explicitly; unlike __str__, there is no inherited
    __call__ default for object instances to defeat __getattr__.
    
    • __len__ is caught by both classes, simply because it is an explicitly defined method
    in the classes themselves—though its name it is not routed to either __getattr__
    or __getattribute__ in 3.X if we delete the class’s __len__ methods.
    
    • All other built-in operations fail to be intercepted by both schemes in 3.X.
"""



'''
Again, the net effect is that operator overloading methods implicitly run by built-in
operations are never routed through either attribute interception method in 3.X: Python
3.X’s new-style classes search for such attributes in classes and skip instance lookup
entirely. Normally named attributes do not.

This makes delegation-based wrapper classes more difficult to code in 3.X’s new-style
classes—if wrapped classes may contain operator overloading methods, those methods
must be redefined redundantly in the wrapper class in order to delegate to the wrapped
object. In general delegation tools, this can add dozens of extra methods.

Of course, the addition of such methods can be partly automated by tools that augment
classes with new methods (the class decorators and metaclasses of the next two chapters
might help here). Moreover, a superclass might be able to define all these extra methods
once, for inheritance in delegation-based classes. Still, delegation coding patterns require
extra work in 3.X’s classes.
'''
