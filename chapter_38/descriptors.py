"Descriptors"
'''
Descriptors provide an alternative way to intercept attribute access; they are strongly
related to the properties. Really, a property is a kind of
descriptor—technically speaking, the property built-in is just a simplified way to create
a specific type of descriptor that runs method functions on attribute accesses. In fact,
descriptors are the underlying implementation mechanism for a variety of class tools,
including both properties and slots.

Functionally speaking, the descriptor protocol allows us to route a specific attribute’s
get, set, and delete operations to methods of a separate class’s instance object that we
provide. This allows us to insert code to be run automatically on attribute fetches and
assignments, intercept attribute deletions, and provide documentation for the attributes
if desired.

a descriptor may call methods available in the client class, as well as descriptorspecific
methods it defines.

Like a property, a descriptor manages a single, specific attribute; although it can’t catch
all attribute accesses generically, it provides control over both fetch and assignment
accesses and allows us to change an attribute name freely from simple data to a computation
without breaking existing code. Properties really are just a convenient way to
create a specific kind of descriptor.
'''

"""
Unlike properties, descriptors are broader in scope, and provide a more general tool.
For instance, because they are coded as normal classes, descriptors have their own state,
may participate in descriptor inheritance hierarchies, can use composition to aggregate
objects, and provide a natural structure for coding internal methods and attribute documentation
strings.
"""

'The Basics'
'''
descriptors are coded as separate classes and provide specially
named accessor methods for the attribute access operations they wish to intercept
—get, set, and deletion methods in the descriptor class are automatically run when the
attribute assigned to the descriptor class instance is accessed in the corresponding way:
'''
class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): ...                         # Return attr value
    def __set__(self, instance, value): ...                         # Return nothing(None)
    def __delete__(self, instance, value): ...                      # Return nothing(None)


"""
Classes with any of these methods are considered descriptors, and their methods are
special when one of their instances is assigned to another class’s attribute—when the
attribute is accessed, they are automatically invoked. If any of these methods are absent,
it generally means that the corresponding type of access is not supported. Unlike properties,
however, omitting a __set__ allows the descriptor attribute’s name to be assigned
and thus redefined in an instance, thereby hiding the descriptor—to make an attribute
read-only, you must define __set__ to catch assignments and raise an exception.

In short, a descriptor with a __set__ is known formally
as data descriptor, and is given precedence over other names located by normal inheritance
rules. The inherited descriptor for name __class__, for example, overrides the
same name in an instance’s namespace dictionary. This also works to ensure that data
descriptors you code in your own classes take precedence over others.
"""


'Descriptor method arguments'
""" 
Before we code anything realistic, let’s take a brief look at some fundamentals. All three
descriptor methods outlined in the prior section are passed both the descriptor class
instance (self), and the instance of the client class to which the descriptor instance is
attached (instance).
""" 
# The descriptor knows it is being accessed directly 
# when its instance argument is None
class Descriptor:
    def __get__(self, instance, owner):
            print(self, instance, owner, sep='\n')
    
class Subject:
    attr = Descriptor()

X = Subject()
print(X.attr)                                               # X.attr -> Descriptor.__get__(Subject.attr, X, Subject)


'Read-only descriptors'
"""
unlike properties, simply omitting the __set__ method in a descriptor
isn’t enough to make an attribute read-only, because the descriptor name can
be assigned to an instance.
"""
class D:
    def __get__(*args): print('get')

class C:
    a = D()                                                 # Attribute a is a descriptor instance

X = C() 
print(X.a)                                                  # Runs inherited descriptor __get__
print(C.a)

X.a = 99                                                    # Stored on X, hiding C.a!
print(X.a)
print(list(X.__dict__.keys()))

Y = C()
print(Y.a)                                                  # Y still inherits descriptor
print(C.a)


"""
This is the way all instance attribute assignments work in Python, and it allows classes
to selectively override class-level defaults in their instances. To make a descriptor-based
attribute read-only, catch the assignment in the descriptor class and raise an exception
to prevent attribute assignment—when assigning an attribute that is a descriptor,
Python effectively bypasses the normal instance-level assignment behavior and routes
the operation to the descriptor object:
"""
class D:
    def __get__(*args): print('get') 
    def __set__(*args): raise ArithmeticError('cannot set')

class C:
    a = D()

X = C() 
print(X.a)                                                      # Routed to C.a.__get__
# X.a = 99                                                      # Routed to C.a.__set__; AttributeError: cannot set

