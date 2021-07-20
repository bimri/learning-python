"__getattribute__ and Descriptors: Attribute Tools"
""" 
the __getattribute__ operator overloading
method, available for new-style classes only, allows a class to intercept all attribute
references, not just undefined references. This makes it more potent than its __get
attr__ cousin, but also trickier to use—it’s prone to loops
much like __setattr__, but in different ways.

Python supports the notion of attribute descriptors—classes with
__get__ and __set__ methods, assigned to class attributes and inherited by instances,
that intercept read and write accesses to specific attributes.
"""
class AgeDesc(object): 
    def __get__(self, instance, owner): return 40 
    def __set__(self, instance, value): instance._age = value


class descriptors(object):
    age = AgeDesc()


x = descriptors() 
print(x.age)                                                # Runs AgeDesc.__get__

x.age = 42                                                  # Runs AgeDesc.__set__
print(x._age)                                               # Normal fetch: no AgeDesc call 

'''
Descriptors have access to state in instances of themselves as well as their client class,
and are in a sense a more general form of properties; in fact, properties are a simplified
way to define a specific type of descriptor—one that runs functions on access.
'''

