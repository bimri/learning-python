print(1 > 2, 1 < 2)             # Booleans
print(bool('spam'))             # Object's Boolean value

X = None                        # None placeholder
print(X)

L = [None] * 100                # Initialize a list of 100 names
print(L)



# types are classes and vice versa
if isinstance(L, list):
    print('yes')

if type(L) == list:
    print('yes')

if type(L) == type([]):
    print('yes')
