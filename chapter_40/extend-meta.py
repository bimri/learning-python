"Metaclass-Based Augmentation"
'''
Although manual augmentation works, in larger programs it would be better if we could
apply such changes to an entire set of classes automatically. That way, we’d avoid the
chance of the augmentation being botched for any given class. Moreover, coding the
augmentation in a single location better supports future changes—all classes in the set
will pick up changes automatically.

One way to meet this goal is to use metaclasses. If we code the augmentation in a
metaclass, every class that declares that metaclass will be augmented uniformly and
correctly and will automatically pick up any changes made in the future.
'''
# Extend with a metaclass - supports future changes better

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)

    
class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2
    

class Client2(metaclass=Extender):
    value = 'ni?'


X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


"""
Notice that the metaclass in this example still performs a fairly static task: adding two
known methods to every class that declares it. In fact, if all we need to do is always add
the same two methods to a set of classes, we might as well code them in a normal
superclass and inherit in subclasses. In practice, though, the metaclass structure supports
much more dynamic behavior. For instance, the subject class might also be configured
based upon arbitrary logic at runtime:
"""
# Can also configure class based on runtime tests

class MetaExtend(type):
    def __new__(meta, classname, supers, classdict):
        if sometest():
            classdict['eggs'] = eggsfunc1
        else:
            classdict['eggs'] = eggsfunc2
        if someothertest():
            classdict['ham'] = hamfunc
        else:
            classdict['ham'] = lambda *args: 'Not supported'
        return type.__new__(meta, classname, supers, classdict)
    
