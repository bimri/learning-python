" `ord` function - returns the interger code point of a single character"
" `chr` is the converse - returns the character for an integer code point"

print(ord('b'))

# collect ASCII codes of all characters in a string
res = []
for x in 'bimri':
    res.append(ord(x))                                  # manual results collection

print(res)

# map - for similar results as above
res = list(map(ord, 'Masinde'))                         # Apply function to sequence(or other)
print(res)

# List compre subsititute for similar outcomes above
res = [ord(x) for x in 'Coldplay']                      # Apply expression to sequence (or other)
print(res)


# arbitrary expression to an iterable instead of a function
mth = [x ** 2 for x in range(10)]                       # assign it to a variable if you need to retain it
print(mth)

# map equivalence - invent a lil func to implement square operation
so = list(map((lambda x: x ** 2), range(10)))
print(so)
