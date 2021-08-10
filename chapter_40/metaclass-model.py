"The Metaclass Model"
'Classes Are Instances of type'
'''
Recall that the type built-in returns the type of any object (which is itself an object)
when called with a single argument. For built-in types like lists, the type of the instance
is the built-in list type, but the type of the list type is the type type itself—the type object
at the top of the hierarchy creates specific types, and specific types create instances.
'''

print(
    type([]), type(type([])),                           # List instance is created from list class
)

print(
    type(list), type(type)                              # Same, but with type names
)


'''
As it happens, the type/instance relationship holds true for user-defined classes as well:
instances are created from classes, and classes are created from type. In Python 3.X,
though, the notion of a “type” is merged with the notion of a “class.” In fact, the two
are essentially synonyms—classes are types, and types are classes. That is:
    • Types are defined by classes that derive from type.
    • User-defined classes are instances of type classes.
    • User-defined classes are types that generate instances of their own.

As we saw earlier, this equivalence affects code that tests the type of instances: the type
of an instance is the class from which it was generated. It also has implications for the
way that classes are created that turn out to be the key to this chapter’s subject. Because
classes are normally created from a root type class by default, most programmers don’t
need to think about this type/class equivalence. However, it opens up new possibilities
for customizing both classes and their instances.

For example, all user-defined classes in 3.X (and new-style classes in 2.X) are instances
of the type class, and instance objects are instances of their classes; in fact, classes now
have a __class__ that links to type, just as an instance has a __class__ that links to the
class from which it was made:
'''

class C: pass                                           # 3.X class object (new-style)
X = C()                                                 # Class instance object

print(type(X))                                          # Instance is instance of class
print(X.__class__)                                      # Instance's class
print(type(C))                                          # Class is instance of type
print(C.__class__)                                      # Class's class is type


'''
Notice especially the last two lines here—classes are instances of the type class, just as
normal instances are instances of a user-defined class. This works the same for both
built-ins and user-defined class types in 3.X. In fact, classes are not really a separate
concept at all: they are simply user-defined types, and type itself is defined by a class.
'''
