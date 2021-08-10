"Operator Overloading in Metaclass Methods"
'''
metaclasses may also employ operator overloading to make
built-in operations applicable to their instance classes. The __getitem__ indexing
method in the following metaclass, for example, is a metaclass method designed to
process classes themselves—the classes that are instances of the metaclass, not those
classes’ own later instances.
'''
class A(type):
    def __getitem__(cls, i):                            # Meta method for processing classes:
        return cls.data[i]                              # Built-ins skip class, use meta
                                                        # Explicit names search class + meta


class B(metaclass=A):                                   # Data descriptors in meta used first
    data = 'spam'


B[0]                                                    # Metaclass instance names: visible to class only
B.__getitem__

I = B()
I.data, B.data                                          # Normal inheritance names: visible to instance and class
# I[0]                                                  # TypeError


'''
It’s possible to define a __getattr__ on a metaclass too, but it can be used to process
its instance classes only, not their normal instances—as usual, it’s not even acquired
by a class’s instances:
'''
class A(type):
    def __getattr__(cls, name):                         # Acquired by class B getitem
        return getattr(cls.data, name)                  # But not run same by built-ins


class B(metaclass=A):
    data = 'spam'


B.upper()
B.upper
B.__getattr__

I = B()
# AttributeError
# I.upper
# I.__getattr__


'''
Moving the __getattr__ to a metaclass doesn’t help with its built-in interception shortcomings,
though. In the following continuation, explicit attributes are routed to the
metaclass’s __getattr__, but built-ins are not, despite that fact the indexing is routed
to a metaclass’s __getitem__ in the first example of the section—strongly suggesting
that new-style __getattr__ is a special case of a special case, and further recommending
code simplicity that avoids dependence on such boundary cases:
'''
B.data = [1, 2, 3]
B.append(4) # Explicit normal names routed to meta's getattr
B.data
B.__getitem__(0) # Explicit special names routed to meta's gettarr
# TypeError
# B[0] # But built-ins skip meta's gettatr too?!
