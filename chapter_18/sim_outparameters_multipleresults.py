# return can send back any sort of object, also
# multiple values by packaging them in tuple/other collection type
def multiple(x, y):
    x = 2                       # changes local names only
    y = [3, 4]
    return x, y                 # Return multiple new values in a tuple

X = 1
L = [1, 2]
X, L = multiple(X, L)           # Assign results to caller's names

print(X,L)
