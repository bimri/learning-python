D = {'a':1, 'b':2, 'c':3}

# index a nonexistent key
# print(D['d'])                                               # KeyError

# assign a nonexistent key creates a new dictionary entry
D['d'] = 'spam'

print(D)

'''
Out-of-bounds indexing for lists raises an error too, 
but so do out-of-bounds assignments

Variable names work like dictionary keys; they must have already
been assigned when referenced, but they are created when first assigned

variable names can be processed as dictionary keys if you wish
'''
