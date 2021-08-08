"Coding Class Decorators"
'''
class decorators are really just optional syntactic sugar, though many believe
that they make a programmer’s intent more obvious and minimize erroneous or
missed calls.
'''
'Singleton Classes'
""" 
Because class decorators may intercept instance creation calls, they can be used to either
manage all the instances of a class, or augment the interfaces of those instances. To
demonstrate, here’s a first class decorator example that does the former—managing all
instances of a class. This code implements the classic singleton coding pattern, where
at most one instance of a class ever exists. Its singleton function defines and returns a
function for managing instances, and the @ syntax automatically wraps up a subject
class in this function:
""" 

# 3.X and 2.X: global table

instances = {}

def singleton(aClass):                                      # On @ decoration
    def onCall(*args, **kwargs):                            # On instance creation
        if aClass not in instances:                         # One dict entry per class
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall


# To use this, decorate the classes for which you want to enforce a single-instance model
@singleton                                                  # Person = singleton(Person)
class Person:                                               # Rebinds Person to onCall
    def __init__(self, name, hours, rate):                  # onCall remembers Person
        self.name  = name 
        self.hours = hours
        self.rate  = rate
    def pay(self):
        return self.hours * self.rate 
    

@singleton                                                  # Spam = singleton(Spam)
class Spam:                                                 # Rebinds Spam to onCal1
    def __init__(self, val):
        self.attr = val 
    

bmr = Person('bimri', 78, 10)                               # Really calls onCall
print(bmr.name, bmr.pay())

sue = Person('Sue', 50, 20)                                 # Same, single object
print(sue.name, sue.pay())

X = Spam(val=42)                                            # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)


'''
Now, when the Person or Spam class is later used to create an instance, the wrapping
logic layer provided by the decorator routes instance construction calls to onCall, which
in turn ensures a single instance per class, regardless of how many construction calls
are made.
'''


'Coding alternatives'
""" 
you can code a more self-contained solution here if you’re able to use the
nonlocal statement (available in Python 3.X only) to change enclosing scope names, as
described earlier—the following alternative achieves an identical effect, by using one
enclosing scope per class, instead of one global table entry per class.
""" 
# 3.X only: nonlocal

def singleton(aClass):                                          # On @ decoration
    instance = None
    def onCall(*args, **kwargs):                                # On instance creation
        nonlocal instance                                       # 3.X and later nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs)                  # One scope per class
        return instance
    return onCall


"""
In either Python 3.X or 2.X (2.6 and later), you can also code a self-contained solution
with either function attributes or a class instead. The first of the following codes the
former, leveraging the fact that there will be one onCall function per decoration—the
object namespace serves the same role as an enclosing scope. The second uses one
instance per decoration, rather than an enclosing scope, function object, or global table.
""" 
# 3.X and 2.X: func attrs, classes (alternative codings)

def singleton(aClass):                                              # On @ decoration
    def onCall(*args, **kwargs):                                    # On instance creation
        if onCall.instance == None:
            onCall.instance = aClass(*args, **kwargs)               # One function per class
        return onCall.instance
    onCall.instance = None
    return onCall


class singleton:
    def __init__(self, aClass):                                     # On @ decoration
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):                            # On instance creation
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)            # One instance per class
        return self.instance
        