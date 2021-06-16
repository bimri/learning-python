# Zip together keys and values
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# Make a dict from zip result
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)


# dict comprehension
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)


# map a single stream of values to dictionaries
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)


# Loop over any iterable
D = {c: c * 4 for c in 'BIMRI'}
print(D)

D = {c.lower(): c + '!' for c in ['NYATHI', 'OLUCHI', 'NEKESA']}
print(D)


# initializing dictionaries from keys lists
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)

# Same, but with a comprehension
D = {k:0 for k in ['a', 'b', 'c']}
print(D)

# Other iterables, default value
D = dict.fromkeys('soma')
print(D)

D = {k:None for k in 'SOMA'}
print(D)
