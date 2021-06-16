L = [123, 'spam', 1.23]
print(len(L))                   # get length of collection
print(L[0])                     # item at offset 0
print(L[:-1])                   # all items except last one
print(L + [4, 5, 6])            # concat make new list too
print(L * 2)                    # repeat make new list too
print(L)                        # Original list stays intact


# Lists in py don't have type constraint
# and have no fixed size - they can grow &
# shrink in size.
L.append('NI')           # growing: add object at end of list
print(L)

# pop is equivalent to del statement & removes item at a given offset
L.pop(2)                # shrinking: delete item in the middle
print(L)


# Lists being mutable they can change list objects in place
M = ['bb', 'aa', 'cc']
M.sort()
print(M)

M.reverse()
print(M)

# Nesting
N = [[1,2,3],                       # A 3 x 3 matrix, as nested lists
     [4,5,6],                       # Code can span lines if bracketed
     [7,8,9]]
print(N)
print(N[1])                         # Get row 2
print(N[1][2])                      # Get row 2, then get item 3 within the row


# Comprehensions
col2 = [row[1] for row in N]
print(col2)                             # Collect the items in column 2

print([row[1] + 1 for row in N])                        # add 1 to each item in column 1
print([row[1] for row in N if row[1] % 2 == 0])         # filter out odd items

diag = [N[i][i] for i in [0, 1, 2]]                     # collect a diagonal from matrix
print(diag)

doubles = [c * 2 for c in 'soma']           # repeat chars in a string
print(doubles)


# Collect multipe values with range
# Must be wrapped in a nested collection
print(list(range(10)))              # 0..9 (list() required in 3.X)
print(list(range(-6, 7, 2)))        # −6 to +6 by 2 (need list() in 3.X)


print([[x ** 2, x ** 3] for x in range(4)])     # Multiple values, "if" filters
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])


# Generators from enclosing a comprehension in paratheses
G = (sum(row) for row in N)
print(next(G))                      # Run the iteration protocol next()
print(next(G))
print(next(G))


# map BUILT-IN
print(list(map(sum, N)))            # Map sum over items in N


# Sets & dicts from comptehension syntax
print({sum(row) for row in N})              # Create a set of row sums
print({i : sum(N[i]) for i in range(3)})    # Creates key:value table of row sums


# lists, sets, dictionaries, and generators 
# can all be built with comprehensions
print([ord(x) for x in 'bimri'])                # List of character ordinals
print({ord(x) for x in 'nyathi'})               # Sets remove duplicates
print({x: ord(x) for x in 'koima'})             # Dictionary keys are unique
print((ord(x) for x in 'nekesa'))               # Generator of values
