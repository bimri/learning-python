# 4.A rewrite this code with a loop clause to eliminate the
# flag while else found and final statement if
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')
    

# 4.B For loop with else clause to eliminate the explicit
# list-indexing logic
for p in L:
    if (2 ** X) == p:
        print((2 ** X), 'was found at', L.index(p))
        break
else:
    print(X, 'not found')


# 4.C remove the loop completely - to use "in" membership
# expression
if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')


# 4.D FOR LOOP & list append method to generate powers-of-2 
# list (L) instead of hardcoding a list literal
lst = []

for i in range(10):
    lst.append(2 ** i)
print(lst)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

 
# 4.F LAMBDA and MAP functions to generate powers
L = list(map(lambda x: 2 ** x, range(7)))                       # Or [2 ** X for x in range(&)]
print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')
