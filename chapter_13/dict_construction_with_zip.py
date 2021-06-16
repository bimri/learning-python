D1 = {'spam':1, 'eggs':3, 'toast':5 }
print(D1)

D1 = {}
D1['spam'] = 1
D1['eggs'] = 3
D1['toast'] = 5
print(D1)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

print(
    list(zip(keys, vals))
)

D2 = {}
for (k,v) in zip(keys, vals): D2[k] = v
print(D2)


# Python 2.2 and later you can skip the for loop altogether
D3 = dict(zip(keys, vals))
print(D3)


# dict comprehension, which builds lists in a single expression
dc = {k:v for (k, v) in zip(keys, vals)}
print(dc)
