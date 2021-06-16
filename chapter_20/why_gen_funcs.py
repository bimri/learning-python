# we could also simply build the list of yielded values all at once
def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')
print()

# we could use any of the for loop, map, or list comprehension techniques
for x in [n ** 2 for n in range(5)]:
    print(x, end=' : ')
print()

for x in map((lambda n: n ** 2), range(5)):
    print(x, end=' : ')
print()


"generators can be better in terms of both memory use and performance in larger programs."
# They allow functions to avoid doing all the work up front
"Generators distribute the time required to produce the series of values among loop iterations."
# for more advanced uses, generators can provide a simpler alternative to manually saving the state between iterations in class objects
# —with generators, variables accessible in the function’s scopes are saved and restored automatically
"Generator function can also operate and return any type of object"

def ups(line):
    for sub in line.split(','):             # Substring generator
        yield sub.upper()

print(
    tuple(ups('aaa,bbb,ccc'))               # All iteration contexts
)

print(
    {i:s for (i,s) in enumerate(ups('aaa,bbb,ccc'))}
)
