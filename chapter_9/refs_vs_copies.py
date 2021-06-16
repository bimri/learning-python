# assignments always store references to objects
# not copies of those objects.
X = [1, 2, 3]
L = ['a', X, 'b']                                           # Embed references to X's object
D = {'x':X, 'y':2}

print(X)
print(L)
print(D)

# Changes all three references!
X[1] = 'surprise'

print(L)
print(D)

# you can avoid the reference side effects by slicing the
# original list instead of simply naming it
X = [1, 2, 3]
L = ['a', X[:], 'b']                                # Embed copies of X's object
D = {'x':X[:], 'y':2}


'''changes made from the other variables 
will change the copies, not the originals'''
L = [1,2,3]
D = {'a':1, 'b':2}

A = L[:]                                                # Instead of A = L (or list(L))
B = D.copy()                                            # Instead of B = D (ditto for sets)

A[1] = 'Ni'
B['c'] = 'spam'

print(L,D)
print(A,B)


'''fully independent copy of a deeply nested data structure'''
# import copy
# X = copy.deepcopy(Y)