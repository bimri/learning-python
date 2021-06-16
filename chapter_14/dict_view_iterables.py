'''
the dictionary keys, values, and
items methods return iterable view objects that generate result items one at a time,
instead of producing result lists all at once in memory
'''
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()                                            # A view object in 3.X, not a list
print(K)

# Views are not iterators themselves
# print(next(K))                                        # TypeError: dict_keys object is not an iterator

I = iter(K)                                             # View iterables have an iterator,
print(
    next(I)                                             # which can be used manually,
)

print(
    next(I)                                             # but does not support len(), index
)


# All iteration contexts use auto
for k in D.keys():
    print(k, end=' ')
print()

K = D.keys()
print(
    list(K)                                             # Can still force a real list if needed
)

V = D.values()                                          # Ditto for values() and items() views
print(V)

print(
    list(V)                                             # Need list() to display or index as list
)


# V[0]                                                  # TypeError: 'dict_values' object does not support indexing
print(
    list(V)[0]
)

print(
    list(D.items())
)


for (k, v) in D.items(): print(k, v, end=' ')
print()


'''dictionaries still are iterables themselves
it’s not often necessary to call keys directly in this context'''
print(D)                                                    # Dictionaries still produce an iterator

I = iter(D)
print(next(I))
print(next(I))
print(next(I))

for key in D: print(key, end=' ')                           # Still no need to call keys() to iterate
print()

# convert keys views first with a list call, or use the 
# sorted call on either a keys view or the dictionary itself
print(D)

for k in sorted(D.keys()): print(k, D[k], end=' ')
print()

# "Best practice" key sorting
for k in sorted(D): print(k, D[k], end=' ')
print()
