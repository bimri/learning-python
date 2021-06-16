# simple for loop
S = 'nyathi'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1
print()

# ENUMERATE
S = 'bimri'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

print()


E = enumerate(S)
print(E)
print(next(E))
print(next(E))
print(next(E))
print(next(E))
print(next(E))

print()


# run the iteration protocol automatically
pro = [c * i for (i, c) in enumerate(S)]
print(pro)


for (i, l) in enumerate(open('test.txt')):
    print('%s) %s' % (i, l.rstrip()))

