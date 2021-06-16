L = [0, 1, 2, 3]
print(L)

# print(L[4])                                                                               # IndexError: list index out of range
# slicing out of bounds (e.g., L[-1000:100]) works

print(L[-1000:100])

# Extracting a sequence in reverse, with the lower bound greater than the higher
# bound (e.g., L[3:1]), doesn’t really work.

'''
You get back an empty slice ([ ]) because
Python scales the slice limits to make sure that the lower bound is always less than
or equal to the upper bound (e.g., L[3:1] is scaled to L[3:3], the empty insertion
point at offset 3).

Python slices are always extracted from left to right, even if you
use negative indexes (they are first converted to positive indexes by adding the
sequence length).
'''

print(L[3:1])
print(L)
L[3:1] = ['?']
print(L)

