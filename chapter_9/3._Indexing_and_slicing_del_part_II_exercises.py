L = [1,2,3,4]

# assign an empty list
L[2]=[]
print(L)

L[2:3]=[]
print(L)

# del statement deletes offsets, keys, attributes, and names
del L[0]
print(L)

'''Slice assignment expects another sequence, or you’ll get a type error; it inserts items
inside the sequence assigned, not the sequence itself'''
# L[1:2] = 1                                                        # TypeError: can only assign an iterable
# print(L)
