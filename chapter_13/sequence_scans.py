''' Sequence scans: while and range Versus for'''
# Simple iteration
X = 'spam'

for item in X: print(item, end=' ')
print()

# take over the indexing logic explicitly
i = 0
while i < len(X):                                           # while loop iteration
    print(X[i], end=' ')
    i += 1 
print()

print(X)
print(len(X))                                               # Length of string
print(list(range(len(X))))                                  # All legal offsets into X

# Manual range/len iteration
for i in range(len(X)): print(X[i], end=' ')
print()

# Use simple iteration if you can
for item in X: print(item, end=' ')
