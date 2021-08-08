"Class Blunders II: Retaining Multiple Instances"
"""
Curiously, the decorator function in this example can almost be coded as a class instead
of a function, with the proper operator overloading protocol. The following slightly
simplified alternative works similarly because its __init__ is triggered when the @ decorator
is applied to the class, and its __call__ is triggered when a subject class instance
is created. Our objects are really instances of Tracer this time, and we essentially just
trade an enclosing scope reference for an instance attribute here:
"""
class Tracer:
    def __init__(self, aClass):                     # On @decorator
        self.aClass = aClass                        # Use instance attribute
    def __call__(self, *args):                      # On instance creation
        self.wrapped = self.aClass(*args)           # ONE(LAST) INSTANCE PER CLASS!
        return self 
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname) 
    

@Tracer                                             # Triggers __init__
class Spam:                                         # Like: Spam = Tracer(Spam)
    def display(self):
        print('Spam! ' * 8)

...
food = Spam()                                       # Triggers __call__
food.display()                                      # Triggers __getattr__


'''
As we saw in the abstract earlier, though, this class-only alternative handles multiple
classes as before, but it won’t quite work for multiple instances of a given class: each
instance construction call triggers __call__, which overwrites the prior instance. The
net effect is that Tracer saves just one instance—the last one created.
'''

@Tracer
class Person:                                       # Person = Tracer(Person)
    def __init__(self, name):                       # Wrapper bound to Person
        self.name = name 


'''
This code’s output follows—because this tracer only has a single shared instance, the
second overwrites the first:

The problem here is bad state retention—we make one decorator instance per class,
but not per class instance, such that only the last instance is retained. The solution, as
in our prior class blunder for decorating methods, lies in abandoning class-based decorators.
'''

bmr = Person('Bimri')                               # bmr is really a Wrapper
print(bmr.name)                                     # Wrapper embeds a Person
sue = Person('Sue') 
print(sue.name)                                     # sue overwrites bmr
print(bmr.name)                                     # OOPS: now bmr's name is 'Sue'!
