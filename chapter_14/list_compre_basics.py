# syntax
''' L = [x + 10 for x in L]'''
L = [1, 23, 34]

# list comprehensions are never really required
res = []
for x in L:
    res.append(x * 10)

print(res)
