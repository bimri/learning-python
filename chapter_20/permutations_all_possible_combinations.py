'''
These techniques have many other real-world applications—consider generating attachments
in an email message or points to be plotted in a GUI
Moreover, other types of sequence scrambles serve central roles in other applications, 
from searches to mathematics.
'''

'''
As is, our sequence scrambler is a simple reordering, but some programs warrant
the more exhaustive set of all possible orderings we get from permutations—produced
using recursive functions in both list-builder and generator forms by the following
module file:
'''
# Both functions produce the same results
# though the second defers much of its work until it is asked for a result
def permute1(seq):
    if not seq:                                 # Shuffle any sequence: list
        return [seq]                            # Empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]          # Delete current node
            for x in permute1(rest):            # Permute the others
                res.append(seq[i:i+1] + x)      # Add node at front
        return res 

def permute2(seq):
    if not seq:                                 # Shuffle any sequence generator
        yield seq                               # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]          # Delete current node
            for x in permute2(rest):            # Permute the others
                yield seq[i:i+1] + x            # Add node at front

'''
Permutations produce more orderings than the original shuffler—for N items, we get
N! (factorial) results instead of just N (24 for 4: 4 * 3 * 2 * 1).

that’s why we need recursion here: the number of nested loops is arbitrary, 
and depends on the length of the sequence permuted:
'''

from scramble import scramble 

# Simple scrambles: N
print(
    list(scramble('abc'))
)

'''
The list and generator versions’ results are the same, though the generator minimizes
both space usage and delays for results.
'''
# Permutations larger: N!
print(
    permute1('bimri')
)

# Generate all combinations
print(
    list(permute2('adhis'))
)



# Iterate (iter() not needed)
G = permute2('python')
print(next(G))
print(next(G))
print(next(G))

for x in permute2('joka'): print(x)                     # automatic iteration


"For larger items, the set of all permutations is much larger than the simpler scrambler’s:"
print(
    permute1('bimri') == list(permute2('bimri'))
)

print(
    len(list(permute2('bimri'))), len(list(scramble('bimri')))              # 120, 5
)

print(
    list(scramble('bimri'))
)

print(
    list(permute2('bimri'))
)
