"Counting Instances with Static Methods"
class Spam: 
    numInstances = 0                                                # Use static method for class data 
    def __init__(self): 
        Spam.numInstances += 1
    def printNumInstances(): 
        print("Number of instances: %s" % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)             # this version requires an extra staticmethod call             # Now printNumInstances() is a static method


'''
Using the static method built-in, our code now allows the self-less method to be called
through the class or any instance of it
'''    


if __name__ == "__main__":
    from spam_static import Spam 
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()                                        # Call as simple function
    a.printNumInstances()                                           # Instance argument not passed 


'''
allows subclasses to customize the static method with inheritance—a
more convenient and powerful approach than importing functions from the files in
which superclasses are coded.
'''
class Sub(Spam):
    def printNumInstances():                                        # Override a static method
        print("Extra stuff...")                                     # But call back to original
        Spam.printNumInstances()                                    # Call static method
    printNumInstances = staticmethod(printNumInstances)             # Make printNumInstances a static method


if __name__ == "__main__":
    print()

    from spam_static import Spam, Sub
    a = Sub()
    b = Sub()
    a.printNumInstances()                           # Call from subclass instance 

    Sub.printNumInstances()                         # Call from subclass itself
    Spam.printNumInstances()                        # Call from original/parent class


""" 
Moreover, classes can inherit the static method without redefining it—it is run without
an instance, regardless of where it is defined in a class tree:
""" 
class Other(Spam): pass                                             # Inherit static method verbatim

if __name__ == "__main__":
    print()
    from spam_static import Other
    c = Other()
    c.printNumInstances()


""" 
Notice how this also bumps up the superclass’s instance counter, because its constructor
is inherited and run
"""
