"Metaclasses Versus Class Decorators: Round 3 (and Last)"
# Class decorator factory: apply any decorator to all methods of a class

from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))           # Not __dict__
            return aClass
    return DecoDecorate


@decorateAll(tracer)                                                # Use a class decorator
class Person:                                                       # Applies func decorator to methods
    def __init__(self, name, pay):                                  # Person = decorateAll(..)(Person)
        self.name = name                                            # Person = DecoDecorate(Person)
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())


'''
Notice that the class decorator returns the original, augmented class, not a wrapper
layer for it (as is common when wrapping instance objects instead). As for the metaclass
version, we retain the type of the original class—an instance of Person is an instance of
Person, not of some wrapper class. In fact, this class decorator deals with class creation
only; instance creation calls are not intercepted at all.

This distinction can matter in programs that require type testing for instances to yield
the original class, not a wrapper. When augmenting a class instead of an instance, class
decorators can retain the original class type. The class’s methods are not their original
functions because they are rebound to decorators.
'''


"""
To use this scheme to apply the timer
decorator, for example, either of the last two decoration lines in the following will
suffice if coded just before our class definition—the first uses decorator argument defaults,
and the second provides one explicitly:
"""
# @decorateAll(tracer)                                            # Decorate all with tracer

# @decorateAll(timer())                                           # Decorate all with timer, defaults
# @decorateAll(timer(label='@@'))                                 # Same but pass a decorator argument


"""
Finally, it’s possible to combine decorators such that each runs per method call, but it
will likely require changes to those we’ve coded here. As is, nesting calls to them directly
winds up tracing or timing the other’s creation-time application, listing the two on
separate lines results in tracing or timing the other’s wrapper before running the original
method, and metaclasses seem to fare no better on this front:
"""
# @decorateAll(tracer(timer(label='@@')))                             # Traces applying the timer

# class Person:
# @decorateAll(tracer)                                                # Traces onCall wrapper, times methods
# @decorateAll(timer(label='@@'))
# class Person:
# @decorateAll(timer(label='@@'))
# @decorateAll(tracer)                                                # Times onCall wrapper, traces methods
# class Person:


'''
metaclasses and class decorators are not only often interchangeable,
but also commonly complementary. Both provide advanced but powerful ways to customize
and manage both class and instance objects
'''
