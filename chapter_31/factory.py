"Classes Are Objects: Generic Object Factories"
'''
Because classes are also “first class” objects, it’s easy to pass them around a program,
store them in data structures, and so on. You can also pass classes to functions that
generate arbitrary kinds of objects; such functions are sometimes called factories in
OOP design circles. Factories can be a major undertaking in a strongly typed language
such as C++ but are almost trivial to implement in Python.
'''

# an object generator function called factory; expects to be passed a class object
# along with one or more arguments for the class’s constructor.
def factory(aClass, *pargs, **kargs):                               # Varargs tuple, dict
    return aClass(*pargs, **kargs)                                  # Call aClass(or apply in 2.X only)


class Spam:
    def doit(self, message):
        print(message)
    

class Person:
    def __init__(self, name, job=None):
        self.name = name 
        self.job  = job 
    

object1 = factory(Spam)                                             # Make a Spam object
object2 = factory(Person, "Arthur", "King")                         # Make a Person object
object3 = factory(Person, name='Brian')                             # Ditto, with keywords and default
 

if __name__ == "__main__":
    object1.doit(99)
    print(object2.name, object2.job)
    print(object3.name, object3.job)


"Why Factories?"
'''
Such a factory might allow code to be insulated from the details of
dynamically configured object construction.
'''