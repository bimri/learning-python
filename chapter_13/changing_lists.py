# range Versus Comprehensions
L = [1, 2, 3, 4, 5]

for i in range(len(L)):                     # add one to each item L
    L[i] += 1

print(L)


# equivalent while loop
i = 0
while i < len(L):
    L[i] += 1
    i += 1

print(L)


# list compehension
lc = [x + 1 for x in L]
print(lc)
