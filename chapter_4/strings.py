B = 'Bimri'

# Offset from left to right using indices
print(B[0])
print(B[1])
print(B[2])
print(B[4])

# Backward offseting - from right to left 
# using negative indexes
print(B[-1])
print(B[-2])
print(B[-3])
print(B[-5])


# Negative indexing, THE-HARD-WAY!!!
print(B[len(B)-1])


# Slicing -> generic form = X[I:J]
print(B)
print(B[1:4])
print()
print(B[1:])        # everything past the first(1:len(B))
print(B)
print(B[0:3])       #everything but the last two
print(B[:4])
print(B[:-1])
print(B[:])         # All of B as a top-level copy(0:len(B))
print()

# Concatenation
print(B + ' is coding python basics.\n')

#Repetition 
print(B * 8)


"""Strings are immutable by nature."""
# To change them in-place: - run an expression to make new objects
print()
print(B)

B = 'X' + B[1:]
print(B)
print()


'''Changing Strings in place: by first converting it \
    a list'''

S = 'shrubberry'
L = list(S)             # Expand to a list: [...]

print(L)

L[1] = 'c'              # Change in place
print(''.join(L))       # Join with empty delimeter

print()

O = bytearray(b'oranges')       # A byte/list hybrid
O.extend(b'lemons')             
print(O)

print(O.decode())               # translate to normal string
