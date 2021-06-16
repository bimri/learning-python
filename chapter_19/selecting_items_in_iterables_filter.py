'''
filter and reduce, select an iterable’s
items based on a test function and apply functions to item pairs, respectively
'''
# filter being iterable, like range; requires a list call to
# display all its results.


# filter call below, picks out items in a seq that are >= 0
print(
    list(range(-5, 5))                                                      # Iterable in 3.X
)

print(
    list(filter((lambda x: x > 0), range(-5, 5)))                            # Iterable in 3.X
)

# The statement equivalent
res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

print(res)

# list compre
print(
    [x for x in range(-5, 5) if x > 0]                                      # Use () to generate items
)
