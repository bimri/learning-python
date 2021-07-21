"Counting instances per class with class methods"
'''
In fact, because class methods always receive the lowest class in an instance’s tree:
    • Static methods and explicit class names may be a better solution for processing
    data local to a class.
    • Class methods may be better suited to processing data that may differ for each class
    in a hierarchy.

Code that needs to manage per-class instance counters, for example, might be best off
leveraging class methods. In the following, the top-level superclass uses a class method
to manage state information that varies for and is stored on each class in the tree—
similar in spirit to the way instance methods manage state information that varies per
class instance:
'''
class Spam:
    numInstances = 0
    def count(cls):                                                 # Per-class instance counters
        cls.numInstances += 1                                       # cls is lowest class above instance
    def __init__(self):
        self.count()                                                # Passes self.__class__ to count
    count = classmethod(count)


class Sub(Spam):
    numInstances = 0
    def __init__(self):                                             # Redefines __init__
        Spam.__init__(self)


class Other(Spam):                                                  # Inherits __init__
    numInstances = 0


if __name__ == "__main__":
    from spam_class2 import Spam, Sub, Other
    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.numInstances, y1.numInstances, z1.numInstances)                # Per-class data!
    print(Spam.numInstances, Sub.numInstances, Other.numInstances)         # Class data!
    