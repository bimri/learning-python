class C:                                                            # In Python 3.X
    def __getitem__(self, ix):                                      # Indexing overload method
        print('C index')


class D(C):
    def __getitem__(self, ix):                                      # Redefine to extend here
        print('D index')
        C.__getitem__(self, ix)                                     # Traditional call form works
        super().__getitem__(ix)                                     # Direct name calls work too
        super()[ix]                                                 # But operators do not! (__getattribute__)


if __name__ == "__main__":
    X = C()
    X[99]
    
    X = D()
    X[99]                               # TypeError: 'super' object is not subscriptable


""" 
This behavior is due to the very same new-style —because
the proxy object returned by super uses __getattribute__ to catch and dispatch
later method calls, it fails to intercept the automatic __X__ method invocations run by
built-in operations including expressions, as these begin their search in the class instead
of the instance. This may seem less severe than the multiple-inheritance limitation, but
operators should generally work the same as the equivalent method call, especially for
a built-in like this. Not supporting this adds another exception for super users to confront
and remember.

Other languages’ mileage may vary, but in Python, self is explicit, multiple-inheritance
mix-ins and operator overloading are common, and superclass name updates are rare.
Because super adds an odd special case to the language—one with strange semantics,
limited scope, rigid requirements, and questionable reward—most Python programmers
may be better served by the more broadly applicable traditional call scheme.
""" 
