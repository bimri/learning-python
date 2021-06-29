'''
 In the iterations domain, classes can implement the in membership operator as an
iteration, using either the __iter__ or __getitem__ methods. To support more specific
membership, though, classes may code a __contains__ method—when present, this
method is preferred over __iter__, which is preferred over __getitem__. The __con
tains__ method should define membership as applying to keys for a mapping (and can
use quick lookups), and as a search for sequences.
'''
from __future__ import print_function                                       # 2.X/3.X compatibility


class Iters:
    def __init__(self, value):
        self.data = value
    
    def __getitem__(self, i):                                               # Fallback for iteration
        print('get[%s]:' % i, end='')                                       # Also for index, slice
        return self.data[i]
    
    def __iter__(self):                                                     # Preffered for iteration
        print('iter=> ', end='')                                            # Allows only once active iterator
        self.ix = 0
        return self 
    
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item 
    
    def __contains__(self, x):                                              # Preffered for 'in'
        print('contains: ', end='')
        return x in self.data
    next = __next__                                                         # 2.X/3.X compatibility 


if __name__ == '__main__':
    X = Iters([1,2,3,4,5])                  # Make instance
    print(3 in X)                           # Membership
    for i in X:
        print(i, end=' | ')
    
    print()
    print([i ** 2 for i in X])              # Other iteration contexts
    print(list(map(bin, X)))

    I = iter(X)                             #  Manual iteration (what other contexts do)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break 


'''
—the specific __contains__ intercepts membership, the general __iter__ catches other
iteration contexts such that __next__ (whether explicitly coded or implied by yield) is
called repeatedly, and __getitem__ is never called:

Watch what happens to this code’s output if we comment out its __contains__ method,
though—membership is now routed to the general __iter__ instead:

And finally, here is the output if both __contains__ and __iter__ are commented out
—the indexing __getitem__ fallback is called with successively higher indexes until it
raises IndexError, for membership and other iteration contexts:
'''
