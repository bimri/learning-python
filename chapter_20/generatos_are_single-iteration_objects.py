'''
both generator functions and generator expressions are
their own iterators and thus support just one active iteration
'''
"a generator’s iterator is the generator itself"

G = (c * 4 for c in 'BIMRI')
print(iter(G) is G)                                                 # My iterator is myself: G has __next__

'If you iterate over the results stream manually with multiple iterators, they will all point to the same position:'
G = (c * 4 for c in 'SPAM')                                         # Make a new generator
I1 = iter(G)                                                        # Iterate manually
print(next(I1))
print(next(I1))

I2 = iter(G)                                                        # Second iterator at same position!
print(next(I1))

'Moreover, once any iteration runs to completion, all are exhausted—we have to make a new generator to start again:'
print(list(I1))                                                     # Collect the rest of I1's items
print(next(I2))                                                     # Other iterators exhausted too

I3 = iter(G)                                                        # Ditto for new iterators
print(next(I3))

I3 = iter(c * 4 for c in 'SPAM')                                    # New generator to start over
print(next(I3))

# The same holds true for generator functions
def timesfour(S):
    for c in S:
        yield c * 4
    
G = timesfour('KEMET')                                          # Generator functions work the same way
print(iter(G) is G)

I1, I2 = iter(G), iter(G)
print(next(I1))
print(next(I1))
print(next(I2))                                                 # I2 at same position as I1


'''
This is different from the behavior of some built-in types, which support multiple iterators
and passes and reflect their in-place changes in active iterators:
'''
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I2))                                                 # Changes reflected in iterators
next(I1)                                                        # StopIteration

'''
if you wish to scan a generator’s values multiple times, you must either create a new
generator for each scan or build a rescannable list out of its values a single generator’s
values will be consumed and exhausted after a single pass.
'''