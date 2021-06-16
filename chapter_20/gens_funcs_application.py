"Starred arguments can unpack an iterable into individual arguments"
def f(a, b, c):
    print('%s, %s, and %s' % (a, b, c))

f(90, 88, 45)

# unpack range values: iterables in 3.X
f(*range(3))

# Unpack generators expression values
f(*(i for i in range(3)))


"This applies to dictionaries and views too"
D = dict(a='Bob', b='dev', c=40.5); print(D)

# normal keywords
f(a='Bob', b='dev', c=40.5)

# Unpack dict: key=value
f(**D)

#unpack key indicators
f(*D)

# Unpack view iterator: iterable in 3.X
f(*D.values())


'''
Because the built-in
function in 3.X prints all its variable number of arguments,
print
this also makes the following three forms equivalent—the latter using a
to unpack
*
the results forced from a generator expression (though the second also creates a list of
return values, and the first may leave your cursor at the end of the output line in some
shells, but not in the IDLE GUI):
'''
for x in 'spam': print(x.upper(), end=' ')
list(print(x.upper(), end=' ') for x in 'candy')
print()
print(*(x.upper() for x in 'solids'))





"👇🏾Preview: User-defined iterables in classes👇🏾"
# it is also possible to implement arbitrary user-defined 
# generator objects with classes that conform to the iteration protocol
'''
Such
classes define a special __iter__ method run by the iter built-in function, which in
turn returns an object having a __next__ method run by the next built-in
function:


class SomeIterable:
    def __init__(...): ...          # On iter(): return self or supplemental object
    
    def __next__(...): ...          # On next(): coded here, or in another class

👆🏾👆🏾👆🏾 these classes usually return their objects directly for
single-iteration behavior or a supplemental object with scan-specific state for multiplescan
support.


By coding methods, classes also can make iteration
behavior much more explicit than the “magic” generator objects associated with
built-in types and generator functions and expressions
'''
