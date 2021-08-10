"Metaclasses Versus Class Decorators: Round 2"
# metaclasses are probably best used for class object management

'Decorator-based augmentation'
'''
In pure augmentation cases, decorators can often stand in for metaclasses. For example,
the prior section’s metaclass example, which adds methods to a class on creation, can
also be coded as a class decorator; in this mode, decorators roughly correspond to the
__init__ method of metaclasses, since the class object has already been created by the
time the decorator is invoked. Also as for metaclasses, the original class type is retained,
since no wrapper object layer is inserted.
'''
# Extend with a decorator: same as providing __init__ in a metaclass

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc # Manages class, not instance
    aClass.ham = hamfunc # Equiv to metaclass __init__
    return aClass

@Extender
class Client1: # Client1 = Extender(Client1)
    def __init__(self, value): # Rebound at end of class stmt
        self.value = value
    def spam(self):
        return self.value * 2

@Extender
class Client2:
    value = 'ni?'

X = Client1('Ni!') # X is a Client1 instance
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


"""
In other words, at least in certain cases, decorators can manage classes as easily as
metaclasses. The converse isn’t quite so straightforward, though; metaclasses can be
used to manage instances, but only with a certain amount of extra magic.
"""
