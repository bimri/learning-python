# ZIP and MAP
L1 = [1,2,3,4]
L2 = [5,6,7,8]

print(zip(L1, L2))

# list() required
print(
    list(zip(L1, L2))
)


# Wedded with for loop, it support parallel iterations
for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)


# ZIP with N-ary tuple for N arguments
T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print(T3)

print(
    list(zip(T1, T2, T3))                                   # Three tuples for three arguments
)


'''truncates result tuples at the length of the shortest 
sequence when the zip argument lengths differ'''
S1 = 'abc'
S2 = 'xyz123'

print(
    list(zip(S1, S2))
)
print(S2)


# MAP is a value generator in 3.X map
print(
    list(map(ord, 'bimri'))
)

#  Loop equivalent of above
res = []
for c in 'nyathi': res.append(ord(c))
print(res)
