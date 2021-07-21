'''
class decorators are similar to function decorators, but they are run at the end of a class
statement to rebind a class name to a callable. As such, they can be used to either
manage classes just after they are created, or insert a layer of wrapper logic to manage
instances when they are later created. Symbolically, the code structure:

The class decorator is free to augment the class itself, or return a proxy object that
intercepts later instance construction calls.
'''
def decorator(aClass): ...

@decorator                                                              # Class decoration syntax
class C: ...

"is mapped to the following equivalent:"
def decorator(aClass): ...

class C: ... # Name rebinding equivalent
C = decorator(C)


def count(aClass):
    aClass.numInstances = 0
    return aClass                                                       # Return class itself, instead of a wrapper


@count
class Spam: ...                                                         # Same as Spam = count(Spam) 

@count 
class Sub(Spam): ...                                                    # numInstances = 0 not needed here

@count
class Other(Spam): ...                                                   # numInstances = 0 not needed here

""" 
In fact, as coded, this decorator can be applied to class or functions—it happily returns
the object being defined in either context after initializing the object’s attribute: 
""" 
@count
def spam(): pass                                                        # Like spam = count(spam)

@count 
class Other: pass                                                       # Like Other = count(Other)

print(spam.numInstances)                                                # Both are set to zero
print(Other.numInstances)                                               # Both are set to zero


""" 
class decorators can also manage an object’s entire interface by intercepting construction
calls, and wrapping the new instance object in a proxy that deploys attribute accessor
tools to intercept later requests—a multilevel coding technique
""" 
def decorate(cls):                                                      # On @ decoration 
    class Proxy: 
        def __init__(self, *args):                                      # On instance creation: make a cls 
            self.wrapped = cls(*args) 
        def __getattr__(self, attr):                                    # On attribute fetch: extra ops here 
            return getattr(self.wrapped, name) 
    return Proxy 

@decorator
class C: ...                                                            # Same as C = decorator(C)          
X = C()                                                                 # Makes a Proxy that wraps a C, and catches later X.attr


""" 
Metaclasses 

They provide an alternate model, which routes the creation of a class 
object to a subclass of the top-level type class, at the conclusion of 
a class statement:
""" 
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # ... extra logic here + class creation call ...
        ... 

class C(metaclass=Meta):
    # ...my creation routed to Meta...                              # Like C = Meta('C', (), {...})
    ...
