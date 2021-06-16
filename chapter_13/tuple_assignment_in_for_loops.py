T = [(1,2), (3,4), (5,6)]

for (a,b) in T:                                             # tuple assignment at work
    print(a,b)


# Iterate through both keys & values in dicts using - items.method
D = {'a': 1, 'b': 2, 'c':3}
for key in D:
    print(key, '=>', D[key])                                # Use dict keys iterator and index

print(list(D.items()))


for (key, value) in D.items():
    print(key, '->', value)                                 # Iterate over both keys and values


# Manual assignment equivalent
print(T)

for both in T:
    a, b = both
    print(a, b)


# Nested sequences work too
((a,b), c) = ((1,2), 3)
print(a, b, c)

for ((a,b), c) in [((1,2), 3), ((4,5), 6)]: print(a,b,c)


# generic sequence assignment
for ((a,b), c) in [([1,2], 3), ['XY', 6]]: print(a,b,c)


'''Python 3.X extended sequence assignment in for loops'''
# Tuple assignment
a, b, c = (.1, .2, .3)
print(a, b, c)


# Used in for loop
for (a, b, c) in [(10, 20, 30), (40, 50, 60)]:
    print(a, b, c)


# Extended seq assignment
a, *b, c = (1, 2, 3, 4)
print(a, b, c)

for (a, *b, c) in [(100,200,300,400), (500,600,700,800)]:
    print(a,b,c)
