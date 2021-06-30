class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


if __name__ == "__main__":
    '''
    Notice how the order is reversed in __radd__: self is really on the right of the +, and
    other is on the left. Also note that x and y are instances of the same class here; when
    instances of different classes appear mixed in an expression, Python prefers the class
    of the one on the left. When we add the two instances together, Python runs __add__,
    which in turn triggers __radd__ by simplifying the left operand.
    '''
    x = Commuter1(88)
    y = Commuter1(99)

    print(x + 1)                                # __add__: instance + noninstance
    print(1 + y)                                # __radd__: noninstance + instance

    print(x + y)                                # __add__: instance + instance, triggers __radd__



"Reusing __add__ in __radd__"
'''
For truly commutative operations that do not require special-casing by position, it is
also sometimes sufficient to reuse __add__ for __radd__: either by calling __add__ directly;
by swapping order and re-adding to trigger __add__ indirectly; or by simply
assigning __radd__ to be an alias for __add__ at the top level of the class statement (i.e.,
in the class’s scope).

In all these, right-side instance appearances trigger the single, shared __add__ method,
passing the right operand to self, to be treated the same as a left-side appearance.
'''
class Commuter2:
    def __init__(self, val):
        self.val = val 
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other 
    def __radd__(self, other):
        return self.__add__(other)                          # Call __add__explicitly
    

class Commuter3:
    def __init__(self, val):
        self.val = val 
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other 
    def __radd__(self, other):
        return self + other                                 # Swap order and re-add


class Commuter4:
    def __init__(self, val):
        self.val = val 
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other 
    __radd__ = __add__                                      # Alias: cut out the middleman
    
    
if __name__ == "__main__":
    print()
    x = Commuter2(88)
    y = Commuter3(99)
    z = Commuter4(200)

    print(x + 100)                                
    print(1000 + y)                                

    print(x + y) 
    print(z + 34)     
    print(z + y + x)                          



"Propagating class type"
'''
In more realistic classes where the class type may need to be propagated in results,
things can become trickier: type testing may be required to tell whether it’s safe to
convert and thus avoid nesting.
'''
class Commuter5:                                                # Propagate class type in results
    def __init__(self, val):        
        self.val = val 
    def __add__(self, other):
        if isinstance(other, Commuter5):                        # Type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)                      # Else + result is another Commuter
    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val


if __name__ == "__main__":
    print()
    x = Commuter5(88)
    y = Commuter5(99)

    print(x + 10)                                               # Result is another Commuter instance
    print(10 + y)

    z = x + y                                                   # Not nested: doesn't recur to __radd__
    print(z)

    print(z + 10)
    print(z + z)
    print(z + z + 1)



"To test, the rest of commuter.py"
if __name__ == '__main__':
    print()
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
