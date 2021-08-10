"Tracing with Metaclasses and Decorators"
'''
The manual decoration scheme of the prior section works, but it requires us to add
decoration syntax before each method we wish to trace and to later remove that syntax
when we no longer desire tracing. If we want to trace every method of a class, this can
become tedious in larger programs. In more dynamic contexts where augmentations
depend upon runtime parameters, it may not be possible at all. It would be better if we
could somehow apply the tracer decorator to all of a class’s methods automatically.

With metaclasses, we can do exactly that—because they are run when a class is constructed,
they are a natural place to add decoration wrappers to a class’s methods. By
scanning the class’s attribute dictionary and testing for function objects there, we can
automatically run methods through the decorator and rebind the original names to the
results.
'''
# Metaclass that adds tracing decorator to every method of a client class

from types import FunctionType
from decotools import tracer

class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType: # Method?
                classdict[attr] = tracer(attrval) # Decorate it
            return type.__new__(meta, classname, supers, classdict) # Make class

class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
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
The result you see here is a combination of decorator and metaclass work—the metaclass
automatically applies the function decorator to every method at class creation
time, and the function decorator automatically intercepts method calls in order to print
the trace messages in this output.
'''
