"Overloading class creation calls with metaclasses"
'''
Since they participate in normal OOP mechanics, it’s also possible for metaclasses to
catch the creation call at the end of a class statement directly, by redefining the type
object’s __call__. The redefinitions of both __new__ and __call__ must be careful to
call back to their defaults in type if they mean to make a class in the end, and
__call__ must invoke type to kick off the other two here:
'''
# Classes can catch calls too (but built-ins look in metas, not supers!)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


print('making metaclass')
class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass


print('making class')
class Spam(Eggs, metaclass=SubMeta): # Invoke SubMeta, via SuperMeta.__call__
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


'''
This example is complicated by the fact that it overrides a method invoked by a builtin
operation—in this case, the call run automatically to create a class. Metaclasses are
used to create class objects, but only generate instances of themselves when called in a
metaclass role. Because of this, name lookup with metaclasses may be somewhat different
than what we are accustomed to. The __call__ method, for example, is looked
up by built-ins in the class (a.k.a. type) of an object; for metaclasses, this means the
metaclass of a metaclass!
'''

"""
metaclasses also inherit names from other metaclasses normally,
but as for normal classes, this seems to apply to explicit name fetches only, not to the
implicit lookup of names for built-in operations such as calls.

The metaclass in SubMeta is required to set this link,
though this also kicks off a metaclass construction step for the metaclass itself.
"""
