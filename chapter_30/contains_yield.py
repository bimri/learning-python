class Iters:
    def __init__(self, value):
        self.data = value
    
    def __getitem__(self, i):                                               # Fallback for iteration
        print('get[%s]:' % i, end='')                                       # Also for index, slice
        return self.data[i]

    def __iter__(self):                                                     # Preferred for iteration
        print('iter=> next:', end='')                                       # Allows multiple active iterators
        for x in self.data:                                                 # no __next__ to alias to next
            yield x
            print('next:', end='')

    def __contains__(self, x):                                              # Preffered for 'in'
        print('contains: ', end='')
        return x in self.data 
    

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
'''

"""
the __getitem__ method is even more general: besides iterations, it also
intercepts explicit indexing as well as slicing. Slice expressions trigger __getitem__ with
a slice object containing bounds, both for built-in types and user-defined classes, so
slicing is automatic in our class:
"""
if __name__ == '__main__':
    X = Iters('spam')               # Indexing
    print()
    print(X[0])                     # __getitem__(0)

    print('spam'[1:])               # Slice syntax
    print('spam'[slice(1, None)])   # Slice object

    print(X[1:])                    # __getitem__(slice(..))
    print(X[:-1])

    print(list(X))
