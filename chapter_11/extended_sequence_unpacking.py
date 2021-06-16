'''
a single starred name, *X, can be used in the
assignment target in order to specify a more general matching against the sequence—
the starred name is assigned a list, which collects all items in the sequence not assigned
to other names.

        common coding patterns such as splitting
        a sequence into its “front” and “rest,”
'''
seq = [1, 2, 3, 4]

a, b, c, d = seq
print(a, b, c, b)


# a, b = seq                                                      # ValueError: too many values to unpack (expected 2)
a, *b = seq 
print(a)
print(b)


# Starred name
*a, b = seq
print(a)
print(b)

# starred name appears in the middle, it collects
# everything between the other names listed
a, *b, c = seq
print(a)
print(b)
print(c)

# starred name assigned a list of every unassigned
# name at that position
a, b, *c = seq
print(c)


'''
extended sequence unpacking syntax works for any sequence 
types (really, again, any iterable), not just lists
'''
a, *b = 'bimri'
print(a)
print(b)

a, *b, c = 'bimri'
print(a)
print(b)
print(c)


a, *b, c = range(4)
print(a)
print(b)
print(c)


# Slice in similar spirit as above
S = 'spam'
print(S[0], S[1:3], S[3])


# Get first, rest without slicing
L = [1, 2, 3, 4]
while L:
        front, *L = L
        print(front, L)



# Boundary cases
'''the starred name may match just a single item, 
but is always assigned a list'''
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)


a, b, *e, c, d = seq
print(a, b, c, d, e)


'''errors can still be triggered if there is more than one starred name'''
# a, *b, c, *d = seq                                              # SyntaxError: two starred expressions in assignment

# a, b = seq                                                      # ValueError: too many values to unpack (expected 2)

# *a = seq                                                        # SyntaxError: starred assignment target must be in a list or tuple

*a, = seq
print(a)


# “rest, last” splitting pattern
*a, b = seq                                                     # Rest, last
print(a, b)

a, b = seq[:-1], seq[-1]                                        # Rest, last: traditional
print(a, b)


'''Application to for loops'''
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
        pass
# a, *b, c = (1, 2, 3, 4) # b gets [2, 3]
