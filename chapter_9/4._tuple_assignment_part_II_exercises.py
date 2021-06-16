X = 'spam'
Y = 'eggs'
X, Y = Y, X

# The values of X and Y are swapped

'''
When tuples appear on the
left and right of an assignment symbol (=), Python assigns objects on the right to
targets on the left according to their positions

The items on the right are a tuple, which gets unpacked during the assignment
'''

print(X)
print(Y)
