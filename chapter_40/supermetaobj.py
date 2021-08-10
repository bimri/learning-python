"Overloading class creation calls with normal classes"
'''
In fact, we can use normal superclass inheritance to acquire the call interceptor in this
coding model—the superclass here is serving essentially the same role as type, at least
in terms of metaclass dispatch:
'''
# Instances inherit from classes and their supers normally

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs:
    pass


print('making class')
class Spam(Eggs, metaclass=SuperMetaObj()):                                     # # Invoke Sub instance via Super.__call__                                        # MetaObj is normal class instance
    data = 1                                                                    # Called at end of statement
    def meth(self, arg):
        return self.data + arg


print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


"""
Although such alternative forms work, most metaclasses get their work done by redefining
the type superclass’s __new__ and __init__; in practice, this is usually as much
control as is required, and it’s often simpler than other schemes. Moreover, metaclasses
have access to additional tools, such as class methods we’ll explore ahead, which can
influence class behavior more directly than some other schemes.
"""
