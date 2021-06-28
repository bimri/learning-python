'''
the for statement works by repeatedly indexing a sequence from zero to higher indexes,
until an out-of-bounds IndexError exception is detected. Because of that, __geti
tem__ also turns out to be one way to overload iteration in Python—if this method is
defined, for loops call the class’s __getitem__ each time through, with successively
higher offsets.

It’s a case of “code one, get one free”—any built-in or user-defined object that responds
to indexing also responds to for loop iteration:
'''

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]
    

def tester():
    X = StepperIndex()                                  # X is a StepperIndex object
    X.data = "Bimri"
    print(X[1])                                                # Indexing calls __getitem__

    for item in X:                                      # for loops call __getitem__
        print(item, end=' ')                            # for indexes items 0..N
    

if __name__ == '__main__':
    tester()


"Any class that supports for loops automatically supports all iteration contexts in Python"
# All call __getitem__ too
def tester():
    X = StepperIndex()
    X.data = 'LESSON'
    # All call __getitem__ too
    print('B' in X)
    # List comprehension
    print([c for c in X])
    # map calls (use list() in 3.X)
    print(list(map(str.lower, X)))
    # Sequence assignments
    (a, b, c, d, e, f) = X
    print(a, c, d)
    # And so on...
    print(list(X), tuple(X), ''.join(X))

    print(X)


if __name__ == '__main__':
    tester()


"""
In practice, this technique can be used to create objects that provide a sequence interface
and to add logic to built-in sequence type operations
"""
