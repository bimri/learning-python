S1 = 'abc'
S2 = 'xyz123'
print(
    list(zip(S1, S2))                                       # Zip pairs items from iterables
)

# zip pairs items, truncates at shortest
print(list(zip([-2, -1, 0, 1, 2])))                         # Single sequence: 1-ary tuples
print(list(zip([1, 2, 3], [2, 3, 4, 5])))                   # N sequences: N-ary tuples


# map passes paired items to function, truncates
print(list(map(abs, [-2, -1, 0, 1, 2])))                    # Single sequence: 1-ary function
print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))              # N sequences: N-ary function


# map and zip accept arbitrary iterables
print(map(lambda x, y: x + y, open('permute.py'), open('permute.py')))
print([x + y for (x, y) in zip(open('permute.py'), open('permute.py'))])



"Coding your own map(func, ...)"
# map(func, seqs...) workalike with zip
'''
This version relies heavily upon the special *args argument-passing syntax—it collects
multiple sequence (really, iterable) arguments, unpacks them as zip arguments to combine,
and then unpacks the paired zip results as arguments to the passed-in function.
'''
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):                                 # zipping is essentially a nested operation in mapping
        res.append(func(*args))
    return res 

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))

'We can code our map more concisely as an equivalent one-line list comprehension:'
# Using a list comprehension
def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]                 # code is more concise and might run faster

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


# Using generators: yield and (...)
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))



"Coding your own zip(...) and map(None, ...)"
# zip(seqs...) and 2.X map(None, seqs...) workalikes
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))


# Using generators: yield
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

S1, S2 = 'abc', 'xyz123'
print(list(myzip(S1, S2)))
print(list(mymapPad(S1, S2)))
print(list(mymapPad(S1, S2, pad=99)))


# Alternate implementation with lengths
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]

S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))


# Using generators: (...)
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

S1, S2 = 'abc', 'xyz123'
print(list(myzip(S1, S2))) # Go!... [('a', 'x'), ('b', 'y'), ('c', 'z')]
