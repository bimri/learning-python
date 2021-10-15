D = dict(a=1, b=2, c=3)
print(D)

# keys
K = D.keys()
print(K)

print(list(K))

# values
V = D.values()
print(V)

print(list(V))

# items
print(D.items())
print(list(D.items()))

# List operations fail unless converted
# print(K[0]) 
print(list(K)[0])

# Iterators used automatically in loops
for k in D.keys():
    print(k + '\n')


# Still no need to call keys() to iterate
for key in D:
    print(key)


'dynamically reflect future changes'
D = {'a': 1, 'b': 2, 'c': 3}
print(D)

K = D.keys()
V = D.values()
print(list(K))
print(list(V))                                      # Views maintain same order as dictionary

del D['b']                                          # Change the dictionary in place
print(D)
print(list(K))                                      # Reflected in any current view objects
print(list(V))


# Dictionary views and sets
print(K, V)
print(K | {'x': 4})

# TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
# print(V & {'x': 4})

# TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
# V & {'x': 4}.values()


D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & D.keys())                  # Intersect keys views
print(D.keys() & {'b'})                     # Intersect keys and set
print(D.keys() & {'b': 1})                  # Intersect keys and dict
print(D.keys() | {'b', 'c', 'd'})           # Union keys and set


# Items views are set-like too if they are hashable
D = {'a': 1}
print(list(D.items()))                              # Items set-like if hashable
print(D.items() | D.keys())                         # Union view and view
print(D.items() | D)                                # dict treated same as its keys
print(D.items() | {('c', 3), ('d', 4)})             # Set of key/value pairs
print(dict(D.items() | {('c', 3), ('d', 4)}))       # dict accepts iterable sets too
