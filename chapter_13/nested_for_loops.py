items = ["aaa", 111, (4,5), 2.01]                           # a set of objects
tests = [(4,5), 3.14]                                       # keys to search for

for key in tests:                                           # For all keys
    for item in items:                                      # For all items
        if item == key:                                     
            print(key, 'was found')
            break
    else:
        print(key, "not found!")
    

# in-membership to test the inner loop from above
for key in tests:                                           # for all keys
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found')
    

# builds a list as it goes for later use
seq1 = 'spam'
seq2 = 'scam'

res = []                                                    # Start empty
for x in seq1:                                              # Scan first sequence
    if x in seq2:                                           # Common item?
        res.append(x)                                       # Add to result end

print(res)


# generalized into a tool for above code
gen = [x for x in seq1 if x in seq2]                              # Let python collect results
print(gen)
