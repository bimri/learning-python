print((1,2) + (3, 4))               # Concatenation
print((1, 2) * 4)                   # Repetition

T = (1, 2, 3, 4)                    # Indexing, slicing
print(T[0], T[1:3])


# Tuple syntax peculiarities: Commas and parentheses
X = (40)
print(X)                            # An interger

y = (40,)                           # A tuple containing an integer
print(y)


# Conversions, methods, and immutability
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)                       # Make a list from a tuple's items
tmp.sort()                          # Sort the list
print(tmp)
print(T)

T = tuple(tmp)                      # Make a tuple from the list's items
print(T)

print(sorted(T))                    # Or use the sorted built-in, and save two steps


'''List comprehensions can also be used to convert tuples'''
T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)


# index and count
T = (1, 2, 3, 2, 4, 2)              # Tuple methods in 2.6, 3.0, and later
print(T.index(2))

print(T.index(2, 2))                # Offset of appearance after offset 2   
print(T.count(2))                   # How many 2s are there?


'''tuple immutability applies only to the top level of the
        tuple itself, not to its contents'''
T = (1, [2, 3], 4)
# T[1] = 'spam'                 # This fails: can't change tuple itself

T[1][0] = 'spam'                # This works: can change mutables inside
print(T)
