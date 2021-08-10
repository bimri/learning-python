"Inheritance: The Full Story"
'''
As it turns out, instance inheritance works in similar ways, whether the “instance” is
created from a normal class, or is a class created from a metaclass subclass of type—a
single attribute search rule, which fosters the grander and parallel notion of metaclass
inheritance hierarchies. To illustrate the basics of this conceptual merger, in the following,
the instance inherits from all its classes; the class inherits from both classes and
metaclasses; and metaclasses inherit from higher metaclasses (supermetaclasses?):
'''
class M1(type): attr1 = 1                                       # Metaclass inheritance tree
class M2(M1): attr2 = 2                                         # Gets __bases__, __class__, __mro__

class C1: attr3 = 3                                             # Superclass inheritance tree
class C2(C1,metaclass=M2): attr4 = 4                            # Gets __bases__, __class__, __mro__

I = C2()                                                        # I gets __class__ but not others
I.attr3, I.attr4                                                # Instance inherits from super tree

C2.attr1, C2.attr2, C2.attr3, C2.attr4                          # Class gets names from both trees!
M2.attr1, M2.attr2                                              # Metaclass inherits names too!


'''
Both inheritance paths—class and metaclass—employ the same links, though not recursively:
instances do not inherit their class’s metaclass names, but may request them
explicitly:
'''
I.__class__                                                     # Links followed at instance with no __bases__
C2.__bases__

C2.__class__                                                    # Links followed at class after __bases__
M2.__bases__

I.__class__.attr1                                               # Route inheritance to the class's meta tree
# I.attr1                                                       # Though class's __class__ not followed normally

M2.__class__                                                    # Both trees have MROs and instance links
[x.__name__ for x in C2.__mro__]                                # __bases__ tree from I.__class__
[x.__name__ for x in M2.__mro__]                                # __bases__ tree from C2.__class__


'''
If you care about metaclasses, or must use code that does, study these examples, and
then study them again. In effect, inheritance follows __bases__ before following a single
__class__; normal instances have no __bases__; and classes have both—whether normal
or metaclass.
'''


'Python’s inheritance algorithm: The simple version'
""" 
Now that we know about metaclass acquisition, we’re finally able to formalize the
inheritance rules that they augment. Technically, inheritance deploys two distinct but
similar lookup routines, and is based on MROs. Because __bases__ are used to construct
the __mro__ ordering at class creation time, and because a class’s __mro__ includes
itself, the prior section’s generalization is the same as the following—a first-cut definition
of Python’s new-style inheritance algorithm:
"""

'''
To look up an explicit attribute name:
    1. From an instance I, search the instance, then its class, and then all its superclasses,
    using:
        a. The __dict__ of the instance I
        b. The __dict__ of all classes on the __mro__ found at I’s __class__, from left to
        right
    2. From a class C, search the class, then all its superclasses, and then its metaclasses
    tree, using:
        a. The __dict__ of all classes on the __mro__ found at C itself, from left to right
        b. The __dict__ of all metaclasses on the __mro__ found at C’s __class__, from
        left to right
    3. In both rule 1 and 2, give precedence to data descriptors located in step b sources
    (see ahead).
    4. In both rule 1 and 2, skip step a and begin the search at step b for built-in operations
    (see ahead).

The first two steps are followed for normal, explicit attribute fetch only. There are
exceptions for both built-ins and descriptors, both of which we’ll clarify in a moment.
In addition, a __getattr__ or __getattribute__ may also be used for missing or all
names, respectively.
'''


'The descriptors special case'
"""
some descriptors known as data descriptors
—those that define __set__ methods to intercept assignments—are given precedence,
such that their names override other inheritance sources.

This exception serves some practical roles. For example, it is used to ensure that the
special __class__ and __dict__ attributes cannot be redefined by the same names in an
instance’s own __dict__:
"""
class C: pass                                               # Inheritance special case #1...
I = C()                                                     # Class data descriptors have precedence
I.__class__, I.__dict__


I.__dict__['name'] = 'bob'                                  # Dynamic data in the instance
I.__dict__['__class__'] = 'spam'                            # Assign keys, not attributes
I.__dict__['__dict__'] = {}

I.name                                                      # I.name comes from I.__dict__ as usual
                                                            # But I.__class__ and I.__dict__ do not!
I.__class__, I.__dict__                                                            


'''
This data descriptor exception is tested before the preceding two inheritance rules as
a preliminary step, may be more important to Python implementers than Python programmers,
and can be reasonably ignored by most application code in any event—that
is, unless you code data descriptors of your own, which follow the same inheritance
special case precedence rule:
'''
class D:
    def __get__(self, instance, owner): print('__get__')
    def __set__(self, instance, value): print('__set__')


class C: d = D()                                                # Data descriptor attribute
I = C()
I.d                                                             # Inherited data descriptor access
I.d = 1
I.__dict__['d'] = 'spam'                                        # Define same name in instance namespace dict
I.d                                                             # But doesn't hide data descriptor in class!


'''
Conversely, if this descriptor did not define a __set__, the name in the instance’s dictionary
would hide the name in its class instead, per normal inheritance:
'''
class D:
    def __get__(self, instance, owner): print('__get__')


class C: d = D()
I = C()
I.d                                                             # Inherited nondata descriptor access
I.__dict__['d'] = 'spam'                                        # Hides class names per normal inheritance rules
I.d

'''
In both cases, Python automatically runs the descriptor’s __get__ when it’s found by
inheritance, rather than returning the descriptor object itself—part of the attribute
magic we met earlier in the book. The special status afforded to data descriptors, however,
also modifies the meaning of attribute inheritance, and thus the meaning of names
in your code.
'''


'Python’s inheritance algorithm: The somewhat-more-complete version'
"""
To look up an explicit attribute name:
    1. From an instance I, search the instance, its class, and its superclasses, as follows:
        a. Search the __dict__ of all classes on the __mro__ found at I’s __class__
        b. If a data descriptor was found in step a, call it and exit
        c. Else, return a value in the __dict__ of the instance I
        d. Else, call a nondata descriptor or return a value found in step a
    
    2. From a class C, search the class, its superclasses, and its metaclasses tree, as follows:
        a. Search the __dict__ of all metaclasses on the __mro__ found at C’s __class__
        b. If a data descriptor was found in step a, call it and exit
        c. Else, call a descriptor or return a value in the __dict__ of a class on C’s own
        __mro__
        d. Else, call a nondata descriptor or return a value found in step a
    
    3. In both rule 1 and 2, built-in operations essentially use just step a sources (see
    ahead)


Note here again that this applies to normal, explicit attribute fetch only. The implicit
lookup of method names for built-ins doesn’t follow these rules, and essentially uses
just step a sources in both cases, as the next section will demonstrate.

On top of all this, method __getattr__ may be run if defined when an attribute is not
found, and method __getattribute__ may be run for every attribute fetch, though they
are special-case extensions to the name lookup model.
"""


'Assignment inheritance'
"""
For example, when an attribute assignment is run for new-style classes, a data descriptor
with a __set__ method is acquired from a class by inheritance using the MRO, and
has precedence over the normal storage model. In terms of the prior section’s rules:

    • When applied to an instance, such assignments essentially follow steps a through
    c of rule 1, searching the instance’s class tree, though step b calls __set__ instead
    of __get__, and step c stops and stores in the instance instead of attempting a fetch.
    • When applied to a class, such assignments run the same procedure on the class’s
    metaclass tree: roughly the same as rule 2, but step c stops and stores in the class.

Because descriptors are also the basis for other advanced attribute tools such as properties
and slots, this inheritance pre-check on assignment is utilized in multiple contexts.
The net effect is that descriptors are treated as an inheritance special case in newstyle
classes, for both reference and assignment.
"""


'The built-ins special case'
"""
At least that’s almost the full story. As we’ve seen, built-ins don’t follow these rules.
Instances and classes may both be skipped for built-in operations only, as a special case
that differs from normal or explicit name inheritance. Because this is a context-specific
divergence, it’s easier to demonstrate in code than to weave into a single algorithm.
In the following, str is the built-in, __str__ is its explicit name equivalent, and the
instance is skipped for the built-in only:
"""
class C:                                                    # Inheritance special case #2...
    attr = 1                                                # Built-ins skip a step
    def __str__(self): return('class')


I = C()
I.__str__(), str(I)                                         # Both from class if not in instance

I.__str__ = lambda: 'instance'
I.__str__(), str(I)                                         # Explicit=>instance, built-in=>class!

I.attr                                                      # Asymmetric with normal or explicit names
I.attr = 2; I.attr


'''
As we saw in metaclass5.py earlier, the same holds true for classes: explicit names start
at the class, but built-ins start at the class’s class, which is its metaclass, and defaults
to type:
'''
class D(type):
    def __str__(self): return('D class')

class C(D):
    pass    

C.__str__(C), str(C)                                        # Explicit=>super, built-in=>metaclass!


class C(D):
    def __str__(self): return('C class')


C.__str__(C), str(C)                                        # Explicit=>class, built-in=>metaclass!


class C(metaclass=D):
    def __str__(self): return('C class')


C.__str__(C), str(C)                                        # Built-in=>user-defined metaclass


'''
In fact, it can sometimes be nontrivial to know where a name comes from in this model,
since all classes also inherit from object—including the default type metaclass.
In the following’s explicit call, C appears to get a default __str__ from object instead of the
metaclass, per the first source of class inheritance (the class’s own MRO); by contrast,
the built-in skips ahead to the metaclass as before:
'''
class C(metaclass=D):
    pass


C.__str__(C), str(C)                                        # Explicit=>object, built-in=>metaclass

C.__str__

for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])

