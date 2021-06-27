"Abstract superclasses in Python 3.X"
from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self, *args):
        pass 


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass


# X = Super()                                           # TypeError: Can't instantiate abstract class Super with abstract methods action

class Sub(Super): pass 

# X = Sub()                                             # TypeError: Can't instantiate abstract class Sub with abstract methods action

class Sub(Super):
    def action(self):
        print('spam')
    

X = Sub()
X.delegate()
