'''Assignment creates references, Not Copies'''
# shared references to mutable
# objects in your program can matter.

L = [1, 2, 3]
print(L)
# Changing L in place changes what M references
M = ['X', L, 'Y']                                       # Embeded a reference to L
print(M)

L[1] = 9                                                # Changes M too
print(L)
print(M)


''' For lists you can alwyas make top-level copy'''
L = [1, 2, 3]
M = ['X', L[:], 'Y']                                    # Embed a copy of L(or list(L), or L.copy())
L[1] = 9                                                # Changes only L, not M
print(L)
print(M)



'''Repetition Adds One Level Deep'''
# Repeating a sequence is like 
# adding it to itself a number of times
L = [4, 5, 6]
X = L * 4                                             # Like [4, 5, 6] + [4, 5, 6] + ...
Y = [L] * 4                                           # [L] + [L] + ... = [L, L,...]

print(X)
print(Y)


# L was nested in the second repetition
# Y winds up embedding references back to the original list assigned to L
# open to the same sorts of side effects noted in the preceding section
L[1] = 0                                                                                        # Impacts Y but not X
print(X)
print(Y)

# make copies when you don’t want shared references
L = [4, 5, 6]
Y = [list(L)] * 4                                                                               # Embed a (shared) copy of L
L[1] = 0
print(Y)

# Y doesn’t share an object with L anymore, it still embeds
# four references to the same copy of it

Y[0][1] = 99                                                                                    # All four copies are still the same

# you must avoid that sharing too, you’ll want
# to make sure each embedded copy is unique
print(Y)


L = [4,5,6]
Y = [list(L) for i in range(4)]
print(Y)

Y[0][1] = 99
print(Y)



''' Beware of Cyclic Data Structures '''
# If a collection contains a reference to itself,
# it is a cyclic object - Python prints a [...]
L = ['grail']                                           # Append reference to same object
L.append(L)                                             # Generates cycle in object[...]
print(L)


# cyclic structures may cause code of your own to fall into 
# unexpected loops if you don’t anticipate them


'''Immutable Types can't be changed in Place.'''
T = (1, 2, 3)
# T[2] = 4                        # ERROR

T = T[:2] + (4,)                  # OK: (1,2,4)
print(T)
