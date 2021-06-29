"Attribute Access: __getattr__ and __setattr__"
"""
classes can also intercept basic attribute access (a.k.a. qualification) when
needed or useful. Specifically, for an object created from a class, the dot operator expression
object.attribute can be implemented by your code too, for reference, assignment,
and deletion contexts.
"""

"Attribute Reference"
'''
The __getattr__ method intercepts attribute references. It’s called with the attribute
name as a string whenever you try to qualify an instance with an undefined (nonexistent)
attribute name. It is not called if Python can find the attribute using its inheritance tree
search procedure.

Because of its behavior, __getattr__ is useful as a hook for responding to attribute
requests in a generic fashion.

It’s commonly used to delegate calls to embedded (or
“wrapped”) objects from a proxy controller object

This method can also be used to adapt classes to an
interface, or add accessors for data attributes after the fact—logic in a method that
validates or computes an attribute after it’s already being used with simple dot notation.
'''
class Empty:
    def __getattr__(self, attrname):                        # On self.undefined
        if attrname == 'age':
            return 40 
        
        else:
            raise AttributeError(attrname)

    

if __name__ == '__main__':
    X = Empty()
    print(X.age)

    # print(X.name)                     # AttributeError: name
    
