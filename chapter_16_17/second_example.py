"Intersecting Sequences"

# wrapping the code in a function makes it a general 
# intersection utility
'function definition'
def intersect(seq1, seq2):
    res = []                                                # Start empty
    for x in seq1:                                          # Scan seq1
        if x in seq2:                                       # Common item?
            res.append(x)                                   # Add to end
    return res


'function call'
s1 = "BIMRI"
s2 = "bxmrx"

print(
    intersect(s1.lower(), s2)                               # Strings
)


# function could be replaced with 
# a single list comprehension expression
lce = [x for x in s1 if x in s2.upper()]
print(lce)


"intersect func defined above is polymorphic"
# that is, type-dependent behavior!
x = intersect([1, 2, 3], (1, 4))                            # Mixed types
print(x)                                                    # Saved result object
