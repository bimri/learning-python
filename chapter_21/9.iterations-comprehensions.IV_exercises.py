import math

lst = [2, 4, 9, 16, 25]

res = []
for x in lst: res.append(math.sqrt(x))

print(
    list(map(math.sqrt, lst))
)

print(
    [math.sqrt(x) for x in lst]
)

print(
    list(math.sqrt(x) for x in lst)
)
