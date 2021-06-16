def intersect(*args):
    res = []
    for x in args[0]:                           # Scan first sequence
        if x in res: continue                   # Skip duplicates
        for other in args[1:]:                  # For all other args
            if x not in other: break            # Item in each one?
        else:                                   # No: break out of loop
            res.append(x)                       # Yes: add items to end
    return res 

def union(*args):
    res = []
    for seq in args:                            # For all args
        for x in seq:                           # For all nodes
            if not x in res:
                res.append(x)                   # Add new items to result
    return res 


s1, s2, s3 = "SPAM", "SCAM", "SLAM"

print(intersect(s1, s2), union(s1, s2))                 # Two operands
print(intersect([1, 2, 3], (1, 4)))                     # Mixed types
print(intersect(s1, s2, s3))                            # Three operands
print(union(s1, s2, s3))                     


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))
    
tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)

# duplicates won’t appear in either intersection or union results
print(
    intersect([1, 2, 1, 3], (1, 1, 4)),
    union([1, 2, 1, 3], (1, 1, 4)),    
)
tester(intersect, ('ababa', 'abcdefga', 'aaaab'), False)