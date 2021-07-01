"OOP and Delegation: “Wrapper” Proxy Objects"
'''
Beside inheritance and composition, object-oriented programmers often speak of delegation,
which usually implies controller objects that embed other objects to which
they pass off operation requests. The controllers can take care of administrative activities,
such as logging or validating accesses, adding extra steps to interface components,
or monitoring active instances.

In a sense, delegation is a special form of composition, with a single embedded object
managed by a wrapper (sometimes called a proxy) class that retains most or all of the
embedded object’s interface.
'''

class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj                              # Save object
    def __getattr__(self, attrname):                    # gets the attribute name as a string
        print('Trace: ' + attrname)                     # Trace fetch
        return getattr(self.wrapped, attrname)          # Delegate fetch


"""
getattr built-in function to fetch an attribute from the wrapped object by name string
getattr(X,N) is like X.N, except that N is an expression that evaluates to a string at runtime, not a variable
getattr(X,N) is similar to X.__dict__[N],
but the former also performs an inheritance search, like X.N, while the latter does not
"""


'''
You can use the approach of this module’s wrapper class to manage access to any object
with attributes—lists, dictionaries, and even classes and instances. Here, the Wrapper
class simply prints a trace message on each attribute access and delegates the attribute
request to the embedded wrapped object:
'''


if __name__ == "__main__":
    x = Wrapper([1, 2, 3])          # Wrap a list
    x.append(4)                     # Delegate to list method
    print(x.wrapped)

    x = Wrapper({'a': 1, 'b': 2})   # Wrap a dictionary
    list(x.keys())
    
    print(list(x.keys()))
