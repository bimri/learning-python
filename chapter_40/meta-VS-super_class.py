"Metaclass Versus Superclass"
'''
In even simpler terms, watch what happens in the following: as an instance of the A
metaclass type, class B acquires A’s attribute, but this attribute is not made available for
inheritance by B’s own instances—the acquisition of names by metaclass instances is
distinct from the normal inheritance used for class instances:
'''
class A(type): attr = 1
class B(metaclass=A): pass                                      # B is meta instance and acquire meta attr
I = B()

print(B.attr)
# I.attr                                                        # AttributeError
print('attr' in B.__dict__)
print('attr' in A.__dict__)
print()


'''
By contrast, if A morphs from metaclass to superclass, then names inherited from an A
superclass become available to later instances of B, and are located by searching namespace
dictionaries in classes in the tree—that is, by checking the __dict__ of objects in
the method resolution order (MRO)
'''
class A: attr = 1
class B(A): pass                                                # I inherits from class and supers
I = B()

print(B.attr)
print(I.attr)
print('attr' in B.__dict__)
print('attr' in A.__dict__)
print()


"""
This is why metaclasses often do their work by manipulating a new class’s namespace
dictionary, if they wish to influence the behavior of later instance objects—instances
will see names in a class, but not its metaclass. Watch what happens, though, if the
same name is available in both attribute sources—the inheritance name is used instead
of instance acquisition:
"""
class M(type): attr = 1
class A: attr = 2
class B(A, metaclass=M): pass                                   # Supers have precedence over metas
I = B() 

print(B.attr)
print(I.attr)

print('attr' in B.__dict__)
print('attr' in A.__dict__)
print('attr' in M.__dict__)
print()


"""
This is true regardless of the relative height of the inheritance and instance sources—
Python checks the __dict__ of each class on the MRO (inheritance), before falling back
on metaclass acquisition (instance):
"""
class M(type): attr = 1
class A: attr = 2
class B(A): pass
class C(B, metaclass=M): pass                                   # Super two levels above meta: still wins

I = C()
print(I.attr)
print(C.attr)
print([x.__name__ for x in C.__mro__])
print()


"""
In fact, classes acquire metaclass attributes through their __class__ link, in the same
way that normal instances inherit from classes through their __class__, which makes
sense, given that classes are also instances of metaclasses. The chief distinction is that
instance inheritance does not follow a class’s __class__, but instead restricts its scope
to the __dict__ of each class in a tree per the MRO—following __bases__ at each class
only, and using only the instance’s __class__ link once:
"""
print(I.__class__)                                              # Followed by inheritance: instance's class
print(C.__bases__)                                              # Followed by inheritance: class's supers
print(C.__class__)                                              # Followed by instance acquisition: metaclass
print(C.__class__.attr)                                         # Another way to get to metaclass attributes
