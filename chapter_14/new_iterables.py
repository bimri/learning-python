'''The range Iterable'''
R = range(10)                                               # range returns an iterable, not list
print(R)

I = iter(R)                                                 # Make an iterator from the range iterable
print(next(I))
print(next(I))                                              # Advance to next result
print(next(I))                                              # What happens in for loops, comprehensions, etc.

# To force a list if required
print(
    list(range(10))
)


'''The map, zip, and filter Iterables'''
# map returns an iterable, not a list
M = map(abs, (-1, 0, 1))
print(M)

print(next(M))
print(next(M))
print(next(M))
# print(next(M))                                              # stop iteration

# map iterator is now empty: one pass only
for x in M:
    print(x)

# Make a new iterable/iterator to scan again
M = map(abs, (-1, 0, 1))
for x in M:
    print(x)

# Can force a real list if needed
print(list(map(abs, (-1, 0, 1))))


'''ZIP built-in'''
# zip is the same: a one-pass iterator
Z = zip((1, 2, 3), (10, 20, 30))
print(Z)

print(list(Z))

# Exhausted after one pass
for pair in Z: 
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))                            # reassign for a new pass
for pair in Z: print(pair)                                  # Iterator used automatically or manually

# Manual iteration (iter() not needed)
Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))
print(next(Z))


'''The FILTER built-in'''
print(filter(bool, ['spam', '', 'ni']))
print(list(filter(bool, ['spam', '', 'ni'])))

# filter both accepts and returns an iterable to generate results
print(
    [x for x in ['spam', 'ni'] if bool(x)]
)

print(
    [x for x in ['spam', 'ni'] if x]
)