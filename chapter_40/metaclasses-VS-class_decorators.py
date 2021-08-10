"Metaclasses Versus Class Decorators: Round 1"
'''
class decorators described in the
preceding chapter sometimes overlap with metaclasses—in terms of both utility and
benefit. Although they are often used for managing instances, class decorators can also
augment classes, independent of any created instances. Their syntax makes their usage
similarly explicit, and arguably more obvious than manager function calls.
'''
# suppose we coded our manager function to return the augmented class,
# instead of simply modifying it in place.
"This would allow a greater degree of flexibility,"
"because the manager would be free to return any type of object that implements the class’s expected interface:"

def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra 
    

class Client1: ...
Client1 = extras(Client1)

class Client2: ...
Client2 = extras(Client2)

class Client3: ...
Client3 = extras(Client3)

X = Client1()
X.extra()


"""
class decorators’ role in augmenting instance creation
calls. Because they work by automatically rebinding a class name to the result of a
function, though, there’s no reason that we can’t use them to augment the class by
changing it before any instances are ever created. That is, class decorators can apply
extra logic to classes, not just instances, at class creation time:
"""
def extra(self, arg): ...
def extras(Class):
    if required():
        Class.extra = extra
    return Class

@extras
class Client1: ...                                  # Client1 = extras(Client1)

@extras
class Client2: ...                                  # Rebinds class independent of instances

@extras
class Client3: ...

X = Client1()                                       # Makes instance of augmented class
X.extra()                                           # X is instance of original Client1


'''
Decorators essentially automate the prior example’s manual name rebinding here. Just
as for metaclasses, because this decorator returns the original class, instances are made
from it, not from a wrapper object. In fact, instance creation is not intercepted at all in
this example.
'''


"""
Decorators can be used to manage
both instances and classes, and intersect most strongly with metaclasses in the second
of these roles, but this discrimination is not absolute.
"""

"""
decorators technically correspond to metaclass __init__ methods,
used to initialize newly created classes. Metaclasses have additional customization
hooks beyond class initialization, though, and may perform arbitrary class construction
tasks that might be more difficult with decorators. This can make them more complex,
but also better suited for augmenting classes as they are being formed.
"""

'''
metaclasses also have a __new__ method used to create a class, which has
no analogy in decorators; making a new class in a decorator would incur an extra step.
Moreover, metaclasses may also provide behavior acquired by classes in the form of
methods, which have no direct counterpart in decorators either; decorators must provide
class behavior is less direct ways.
'''

'''
Conversely, because metaclasses are designed to manage classes, applying them to
managing instances alone is less optimal. Because they are also responsible for making
the class itself, metaclasses incur this as an extra step in instance management roles.
'''
