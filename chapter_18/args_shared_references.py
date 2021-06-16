def f(a):                               # a is assigned to (references) the passed object
    a = 99                              # Changes local variable a only

b = 88
f(b)                                    # a and b both reference same 88 initially
print(b)                                # b is not changed


def changer(a, b):                      # Arguments assigned references to objects
    a = 2                               # Changes local name's value only
    b[0] = 'spam'                       # Changes shared object in place

X = 1
L = [1, 2]

changer(X, L)                           # Pass immutable and mutable objects
print(X, L)


'''
If we don’t want in-place changes within functions to 
impact objects we pass to them, though, we can simply 
make explicit copies of mutable objects'''
"copy the list at the point of call, with list.copy, or an empty slice:"
L = [1, 2]
changer(X, L[:])                        # Pass a copy, so our 'L' does not change


# copy within the function itself, if we never want to 
# change passed-in objects,regardless of how the function
def changer(a, b):
    b = b[:]                            # Copy input list so we don't impact caller
    a = 2
    b[0] = 'spam'                       # changes our list copy only


'''
Both of these copying schemes don’t stop the function from changing the object—they
just prevent those changes from impacting the caller
'''
L = [1, 2]
# changer(X, tuple(L))                    # Pass a tuple, so changes are errors
