"List comprehensions with if clauses can be thought of as analogous to the filter built-in"
lc = [x for x in range(5) if x % 2 == 0]
print("list comprehension", lc)

fltr = list(filter((lambda x: x % 2 == 0), range(5)))
print("filter", fltr)

# Procedural
res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
    
print("procedural", res)

'''
combine an if clause and an arbitrary expression in our list comprehension, 
to give it the effect of a filter and a map
'''
lcm = [x ** 2 for x in range(10) if x % 2 == 0]
print("list compre", lcm)

# equivalent map call
mp = list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10))))
print("map call", mp)

