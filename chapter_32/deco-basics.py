"Function Decorator Basics"
'''
Syntactically, a function decorator is a sort of runtime declaration about the function
that follows. A function decorator is coded on a line by itself just before the def statement
that defines a function or method. It consists of the @ symbol, followed by what
we call a metafunction—a function (or other callable object) that manages another
function.
'''

class C: 
    @staticmethod                           # Function decoration syntax
    def meth():
        ...

""" 
Internally, this syntax has the same effect as the following—passing the function
through the decorator and assigning the result back to the original name:
""" 

class C: 
    def meth():
        ...
    meth = staticmethod(meth)               # Name rebinding equivalent   


""" 
Decoration rebinds the method name to the decorator’s result. The net effect is that
calling the method function’s name later actually triggers the result of its staticme
thod decorator first. Because a decorator can return any sort of object, this allows the
decorator to insert a layer of logic to be run on every call. The decorator function is free
to return either the original function itself, or a new proxy object that saves the original
function passed to the decorator to be invoked indirectly after the extra logic layer runs.
""" 

class Spam:
    numInstances = 0 
    def __init__(self): 
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)
    

if __name__ == "__main__":
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()                # Calls from classes and instances work
    a.printNumInstances()
    