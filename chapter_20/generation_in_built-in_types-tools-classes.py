"don’t forget that many built-in types behave in similar ways"
'dictionaries are iterables with iterators that produce keys on each  iteration'

D = {'a':1, 'b':2, 'c':3}
x = iter(D)
print(next(x))
print(next(x))

'''
Like the values produced by handcoded generators, dictionary keys may be iterated
over both manually and with automatic iteration tools including for loops, map calls,
list comprehensions
'''
for key in D:
    print(key, D[key])

# for file iterators, Python simply loads lines from the file on demand
for line in open('temp.txt'):
    print(line, end='')


'''
While built-in type iterables are bound to a specific type of value generation, the concept
is similar to the multipurpose generators we code with expressions and functions.
Iteration contexts like for loops accept any iterable that has the expected methods,
whether user-defined or built-in.
'''