X = 1
import mod2 

print(X, end=' ')                           # My global X
print(mod2.X, end=' ')                      # mod2's X
print(mod2.mod3.X)                          # Nested mod3's X


'''
The reverse, however, is not true: mod3 cannot see names in mod2, and mod2 cannot see
names in mod1. This example may be easier to grasp if you don’t think in terms of
namespaces and scopes, but instead focus on the objects involved.

Within mod1, mod2 is just a name that refers to an object with attributes, 
some of which may refer to other objects with attributes (import is an assignment). For paths like mod2.mod3.X, Python
simply evaluates from left to right, fetching attributes from objects along the way.
'''
