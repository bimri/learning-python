nudge = 1                           # Basic assignment
wink  = 2 

A, B = nudge, wink                  # Tuple assignment
print(A, B)                         # Like A = nudge; B = wink

[C, D] = [nudge, wink]              # List assignment
print(C, D)


# Tuples: swaps values
nudge, wink = wink, nudge
print(nudge, wink)


# Assign tuple of values to list of names
[a, b, c] = [1, 2, 3]
print(a, c)

# Assign string of characters to tuple
(a, b, c) = 'ABC'
print(c, b, a)


'''Advanced sequence assignment patterns'''
string = 'BIMRI'
a, b, c, d, e = string
print(b, c, e)

# a, b, c = string                                           # Error if not

# To be more flexible
a, b, c = string[0], string[1], string[2:]
print(c, a)

# Slice and concatenate
a, b, c = list(string[:2]) + [string[2:]]
print(c, b)

# Same, but simpler
a, b = string[:2]
c = string[2:]
print(a, b, c)


# Nested sequences
(a, b), c = string[:2], string[2:]
print(a, b, c)


# Paired by shape and position
((a, b), c) = ('SP', 'AM')
print(a, b, c)


# Simple tuple assignment
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: pass  
# Nested tuple assignment
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: pass


# assigning an integer series to a set of variables
red, green, blue = range(3)
print(red, blue)

r = list(range(3))
print(r)


'''splitting a sequence into its front and the rest in loops'''
L = list(range(6))
while L:
    front, L = L[0], L[1:]
    print(front, L)

