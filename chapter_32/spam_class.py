"Counting Instances with Class Methods"
'''
a class method that
receives the instance’s class in its first argument. Rather than hardcoding the class
name, the class method uses the automatically passed class object generically:
'''
class Spam:
    numInstances = 0                                                    # Use class method instead of static  
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances)
    printNumInstances = classmethod(printNumInstances) 


if __name__ == "__main__": 
    from spam_class import Spam
    a, b = Spam(), Spam() 
    a.printNumInstances()                   # Passes class to fisrt argument
    Spam.printNumInstances()                # Also passes class to fisrt argument

'''
When using class methods, though, keep in mind that they receive the most specific
(i.e., lowest) class of the call’s subject. This has some subtle implications when trying
to update class data through the passed-in class.
'''

class Spam: 
    numInstances = 0                                                   # Trace class passed in 
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances: %s %s' % (cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances) 


class Sub(Spam):
    def printNumInstances(cls):                                         # Override a class method
        print('Extra stuff...', cls)                                    # But call back to original
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)


"lowest class is passed in whenever a class method is run, even for subclasses that have no class methods of their own"
class Other(Spam): pass                                                 # Inherit class method verbatim


if __name__ == "__main__":
    from spam_class import Spam, Sub, Other 
    x = Sub() 
    y = Spam()
    x.printNumInstances()                                # Call from subclass instance
    Sub.printNumInstances()                              # Call from subclass itself
    y.printNumInstances()                                # Call from superclass/parent class 

    "Python passes the lowest class"
    z = Other()                                          # Call from lower sub's instance 
    z.printNumInstances()
