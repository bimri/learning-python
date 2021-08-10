'Overloading class creation calls with normal classes'
""" 
Because normal class instances can respond to call operations with operator overloading,
they can serve in some metaclass roles too, much like the preceding function. The
output of the following is similar to the prior class-based versions, but it’s based on a
simple class—one that doesn’t inherit from type at all, and provides a __call__ for its
instances that catches the metaclass call using normal operator overloading. Note that
__new__ and __init__ must have different names here, or else they will run when the
Meta instance is created, not when it is later called in the role of metaclass:
"""
# A normal class instance can serve as a metaclass too

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class
    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass


print('making class')
class Spam(Eggs, metaclass=MetaObj()):                                          # MetaObj is normal class instance
    data = 1                                                                    # Called at end of statement
    def meth(self, arg):
        return self.data + arg


print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


"""
When run, the three methods are dispatched via the normal instance’s __call__ inherited
from its normal class, but without any dependence on type dispatch mechanics or
semantics:
"""
