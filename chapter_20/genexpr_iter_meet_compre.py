'''
The notion of iterables & list comprehensions 
are combined  in a new tool: GENERATOR EXPRESSIONS
'''
# Syntactically, generator expressions are just like normal list comprehensions

# List comprehension: build a list
[x ** 2 for x in range(4)]

# Generator expression: make an iterable
(x ** 2 for x in range(4))

'''
coding a list comprehension is essentially the
same as wrapping a generator expression in a
built-in call to force it to produce
list all its results in a list at once'''
# List comprehension equivalence
list(x ** 2 for x in range(4))


"looking under the hood at the protocol that these objects automatically support can help demystify them"
G = (x ** 2 for x in range(4))

# iter(G) optional: __iter__ returns self
print(iter(G) is G)

# Generator objects: automatic methods
print(next(G))
print(next(G))
print(next(G))
print(next(G))

print(G)

'''
we don’t typically see the next iterator machinery under the hood of a generator
expression like this because for loops trigger it for us automatically:
'''
# Calls next() automatically
for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2.0))

# eploys generator expressions in the string join method call and tuple assignment, iteration contexts both
print(
    ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
)

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, c)
