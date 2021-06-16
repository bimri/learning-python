'''classic way to step through the keys of a dictionary, for example, is to request its
keys list explicitly'''

D = {'a':1, 'b':2, 'c':3}

for key in D.keys():
    print(key, D[key])


'''In recent versions, dictionaries are iterables with an iterator'''
I = iter(D)

print(next(I))
print(I)
print(next(I))
print(I)
print(next(I))
print(I)
# print(next(I))                      # StopIteration

print('\n')

# Most recent, no need to call the key method(D.keys())
for key in D:
    print(key, D[key])

print('\n')


'''Other Python objects that support the iteration protocol'''
#SHELVES are iterables

import os
P = os.popen('dir')

print(P.__next__())
print(P.__next__())
print(P.__next__())
print(P.__next__())

# TypeError: _wrap_close object is not an iterator
# print(next(P))

print('\n')


'''top-level call iter'''
P = os.popen('dir')
I = iter(P)

print(next(I))
print(next(I))
print(next(I))


# RANGEs are iterables in 3.X
R = range(90)
print(R)

I = iter(R)                                 # Use iteration protocol to produce results

print(next(I))
print(next(I))
print(next(I))

# Or use list to collect all results at once
print(
    list(range(90))
)
print('\n')


# ENUMERATE is an iterable too
E = enumerate('bimri')
print(E)

I = iter(E)
print(next(I))                                  # Generate results with iteration protocol
print(next(I))
print(next(I))
print(next(I))
print(next(I))