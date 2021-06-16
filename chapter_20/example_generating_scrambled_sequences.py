'''
Because they slice and concatenate objects, all the examples in the
section (including the permutations at the end) work only on sequences like strings and
list, not on arbitrary iterables like files, maps, and other generators.

That is, some of these examples will be generators themselves, producing values on request, but they
cannot process generators as their inputs.
'''

"Scrambling sequences"
'''
we can reorder a sequence with slicing and concatenation,
moving the front item to the end on each loop; slicing instead of indexing the item
allows + to work for arbitrary sequence types:
'''
L, S = [1, 2, 3], 'spam'

for i in range(len(S)):                 # For repeat counts 0..3
    S = S[1:] + S[:1]                   # Move front item to the end
    print(S, end=' ')
print()

for i in range(len(L)):
    L = L[1:] + L[:1]                   # Slice so any sequence type works
    print(L, end=' ')
print()


# moving an entire front section to the end, though the order of the results varies slightly:
for i in range(len(S)):                 # For positions 0..3
    X = S[i:] + S[:i]                   # Rear part + front part (same effect)
    print(X, end=' ')
print()



"Simple functions"
# this code works on specific named variables only
'To generalize, we can turn it into a simple function to work on any object passed to its argument and return a result;'
def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

print(scramble('bimri'))


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

print(scramble('adhis'))

for x in scramble((1,2,3,4)):
    print(x, end=' ')



"Generator functions"
'Generator functions retain their local scope state while active, minimize memory space requirements,'
'and divide the work into shorter time slices.'
# As full functions, they are also very general.
def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]                             # Generator function
        yield seq                                           # Assignments work here

def scramble(seq):
    for i in range(len(seq)):                               # Generator function
        yield seq[i:] + seq[:i]                             # Yield one item per iteration
    

list(scramble('Atieno'))                                    # list()generates all results
list(scramble((1,2,3,4)))                                   # Any sequence type works

for x in scramble((1,2,3,4)):                               # for loops generate results
    print(x, end=' ')
print()



"Generator expressions"
'They’re not as flexible as full functions, but because they yield their values automatically,'
'expressions can often be more concise in specific use cases'
S = 'Adhis'
print(S)

G = (S[i:] + S[:i] for i in range(len(S)))                  # Generator expression equivalenent
print(
    list(G)
)
'''
we can’t use the assignment statement of the first generator function version
here, because generator expressions cannot contain statements. This makes them a bit
narrower in scope;

To generalize a generator expression for an arbitrary subject, wrap it in a simple
function that takes an argument and returns a generator that uses it:
'''
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S))
print(list(F(S)))

for x in F((1, 2, 3)): print(x, end=' ')



"Tester client"
# produce scrambled arguments
def scramble(seq):
    for i in range(len(seq)):                                   # Generator function
        yield seq[i:] + seq[:i]                                 # Yield one item per iteration

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

def tester(func, items, trace=True):
    for args in scramble(items):                                # Use generator (or: scrambnle2(items))
        if trace: print(args)
        print(sorted(func(*args)))

# tester(intersect, ('aab', 'abcde', 'ababab'))
# tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False)
