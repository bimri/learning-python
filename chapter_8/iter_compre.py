print(3 in [1, 2, 3])               # Membership

for z in [1, 2, 3]:
    print(z, end=' ')

print()

# List comprehension
res = [c * 4 for c in 'BIMRI'] 
print(res)

# Equivalnent of a for loop to express same code
res = []
for c in 'FOR LOOP':
    res.append(c * 4)

print()
print(res)


# map built-in does the same work
print(list(map(abs, [-1, -2, 0, 1, 2])))            # Map a function across a sequence
