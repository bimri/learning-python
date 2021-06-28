# a method to intercept instance construction (__init__)
# one for catching subtraction expressions (__sub__)

class Number:
    def __init__(self, start):                              # On Number(start)
        self.data = start 
    def __sub__(self, other):                               # On instance - other
        return Number(self.data - other)                    # Result is a new instance
    

if __name__ == '__main__':
    X = Number(5)                                           # Number.__init__(X, 5)
    Y = X - 2                                               # Number.__sub__(X, @)
    print(Y.data)


'''
Technically, instance creation first triggers the __new__ method, which
creates and returns the new instance object, which is then passed into
__init__ for initialization. Since __new__ has a built-in implementation
and is redefined in only very limited roles, though, nearly all Python
classes initialize by defining an __init__ method.

We’ll see one use case
for __new__ when we study metaclasses in Chapter 40; though rare, it is
sometimes also used to customize creation of instances of mutable
types.
'''
