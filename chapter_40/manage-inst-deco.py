"Managing instances instead of classes"
'''
class decorators can often serve the same class-management role as
metaclasses. Metaclasses can often serve the same instance-management role as decorators,
too, but this requires extra code and may seem less natural. That is:
    • Class decorators can manage both classes and instances, but don’t create classes
    normally.

    • Metaclasses can manage both classes and instances, but instances require extra
    work.
'''

"""
For example,
consider the following class decorator example from the prior chapter; it’s used to print
a trace message whenever any normally named attribute of a class instance is fetched:
"""
# Class decorator to trace external instance attribute fetches

def Tracer(aClass):                                         # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):                 # On instance creation
            self.wrapped = aClass(*args, **kargs)           # Use enclosing scope name
        def __getattr__(self, attrname):
            print('Trace:', attrname)                       # Catches all but .wrapped
            return getattr(self.wrapped, attrname)          # Delegate to wrapped object
    return Wrapper


@Tracer
class Person: # Person = Tracer(Person)
    def __init__(self, name, hours, rate):                  # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                                    # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate


bob = Person('Bob', 40, 50)                                 # bob is really a Wrapper
print(bob.name)                                             # Wrapper embeds a Person
print(bob.pay())                                            # Triggers __getattr__


"""
Although it’s possible for a metaclass to achieve the same effect, it seems less straightforward
conceptually. Metaclasses are designed explicitly to manage class object creation,
and they have an interface tailored for this purpose. To use a metaclass just to
manage instances, we have to also take on responsibility for creating the class too—an
extra step if normal class creation would otherwise suffice.
"""
# Manage instances like the prior example, but with a metaclass

def Tracer(classname, supers, classdict):                       # On class creation call
    aClass = type(classname, supers, classdict)                 # Make client class
    class Wrapper:
        def __init__(self, *args, **kargs):                     # On instance creation
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace:', attrname)                           # Catches all but .wrapped
            return getattr(self.wrapped, attrname)              # Delegate to wrapped object
    return Wrapper

class Person(metaclass=Tracer):                                 # Make Person with Tracer
    def __init__(self, name, hours, rate):                      # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                                        # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate
bob = Person('Bob', 40, 50)                                     # bob is really a Wrapper
print(bob.name)                                                 # Wrapper embeds a Person
print(bob.pay())                                                # Triggers __getattr__


'''
This works, but it relies on two tricks. First, it must use a simple function instead of a
class, because type subclasses must adhere to object creation protocols. Second, it must
manually create the subject class by calling type manually; it needs to return an instance
wrapper, but metaclasses are also responsible for creating and returning the subject
class. Really, we’re using the metaclass protocol to imitate decorators in this example,
rather than vice versa; because both run at the conclusion of a class statement, in many
roles they are just variations on a theme.
'''

""" 
metaclasses are probably best suited to class management, due to
their design; class decorators can manage either instances or classes, though they may
not be the best option for more advanced metaclass roles
"""


'Metaclass and class decorator equivalence?'
"""
metaclasses incur an extra step to create the class
when used in instance management roles, and hence can’t quite subsume decorators
in all use cases. But what about the inverse—are decorators a replacement for metaclasses?
"""
# A decorator can call a metaclass, though not vice versa without type()

class Metaclass(type):
    def __new__(meta, clsname, supers, attrdict):
        print('In M.__new__:')
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)


def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))


class A:
    x = 1


@decorator
class B(A):
    y = 2
    def m(self): return self.x + self.y


"""
Again, decorators essentially serve the same role as
metaclass __init__ methods. Because this decorator returns a metaclass instance
"""
# class B(A, metaclass=Metaclass): ...                              # Same effect, but makes just one class


'''
there is some tool redundancy here, and decorator and metaclass roles often overlap
in practice. And although decorators don’t directly support the notion of class-level
methods in metaclasses
'''


"""
The inverse may not seem applicable—a metaclass can’t generally defer to a nonmetaclass
decorator, because the class doesn’t yet exist until the metaclass call completes
—although a metaclass can take the form of a simple callable that invokes type to create
the class directly and passes it on to the decorator. In other words, the crucial hook in
the model is the type call issued for class construction. Given that, metaclasses and
class decorators are often functionally equivalent, with varying dispatch protocol models:
"""
def Metaclass(clsname, supers, attrdict):
    return decorator(type(clsname, supers, attrdict))

def decorator(cls): ...
class B(A, metaclass=Metaclass): ...                                # Metas can call decos and vice versa


'''
In fact, metaclasses need not necessarily return a type instance either—any object
compatible with the class coder’s expectations will do—and this further blurs the decorator/
metaclass distinction:
'''
def func(name, supers, attrs):
    return 'spam'

class C(metaclass=func):                                            # A class whose metaclass makes it a string!
    attr = 'huh?'


C, C.upper()

def func(cls):
    return 'spam'

@func
class C:                                                            # A class whose decorator makes it a string!
    attr = 'huh?'    


C, C.upper()


'''
Odd metaclass and decorator tricks like these aside, timing often determines roles in
practice, as stated earlier:
    • Because decorators run after a class is created, they incur an extra runtime step in
    class creation roles.

    • Because metaclasses must create classes, they incur an extra coding step in instance
    management roles.
'''

"""
In other words, neither completely subsumes the other. Strictly speaking, metaclasses
might be a functional superset, as they can call decorators during class creation; but
metaclasses can also be substantially heavier to understand and code, and many roles
intersect completely.
"""
