"Why the Special Methods?"
'''
makes a first attempt—its class has
a counter stored as a class attribute, a constructor that bumps up the counter by one
each time a new instance is created, and a method that displays the counter’s value.
Remember, class attributes are shared by all instances.
'''
class Spam: 
    numInstance = 0 
    def __init__(self):
        Spam.numInstance = Spam.numInstance + 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstance)


if __name__ == "__main__":
    from spam import Spam
    a = Spam()                          # Cannot call unbound class methods in 2.X 
    b = Spam()                          # Methods expect a self object by default
    c = Spam()

    # Spam.printNumInstances()
    # a.printNumInstances()             # Fails in both 2.X and 3.X (unless static)
    

""" 
if you just want to call functions
that access class members without an instance, perhaps the simplest idea is to use
normal functions outside the class, not class methods. 
""" 
# def printNumInstance(): 
#     print("Number of instances created: %s" % Spam.numInstance)

# class Spam: 
#     numInstances = 0 
#     def __init__(self):
#         Spam.numInstances = Spam.numInstances + 1
    

# if __name__ == "__main__":
#     import spam  
#     a = spam.Spam()
#     b = spam.Spam()
#     c = spam.Spam()

#     spam.printNumInstance()             # But function may be too far removed
#                                         # And cannot be changed via inheritance
#     spam.Spam.numInstances 


class Spam2:
    numInstances = 0 
    def __init__(self):
        Spam2.numInstances = Spam2.numInstances + 1
    def printNumInstances(self):
        print("Number of instances created: %s" % Spam2.numInstances)
    

if __name__ == "__main__":
    from spam import Spam2
    a, b, c = Spam2(), Spam2(), Spam2() 
    a.printNumInstances() 
    Spam2.printNumInstances(a)
    Spam2().printNumInstances()              # But fetching counter changes counter! 
