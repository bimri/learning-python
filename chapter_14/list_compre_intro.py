L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] *= 10

print(L)

# List comprehension of above code(not simiilar though for it makes a new list object)
L = [x * 100 for x in L]
print(L)
