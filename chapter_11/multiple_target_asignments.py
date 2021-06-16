'''A multiple-target assignment simply assigns all the 
given names to the object all the way to the right'''
a = b = c = 'spam'                                          # there is just one object here shared by all three variables
print(a, b, c)

# This form is equivalent to:
c = 'spam'
b = c 
a = b


# behavior is fine for immutable types
a = b = 0
b = b + 1
print(a, b)


# be careful while initializing variables to an empty 
# mutable object e.g. list or dictionary
a = b = []
b.append(42)
print(a, b)

# a and b do not share the same object
a = []
b = []
b.append(42)
print(a, b)

# tuple assignment
a, b = [], []                                               # a and b do not share the same object
print(a, b)
