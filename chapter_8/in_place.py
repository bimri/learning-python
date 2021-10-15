'''
Because lists are mutable, they support operations 
that change a list object in place
'''

# You can change a list's contents by assigning to either
# a particular item(offset) or an entire section(slice)
L = ['AMD', 'OFFICE', 'BIMRI']
print(L)

L[1] = 'Soy'                                                # Index assignment
print(L)

L[0:2] = ['oxridge', 'adapter']                             # Slice assignment: delete+insert
print(L)


# Slice assignment
L = [1, 2, 3]
print(L)

L[1:2] = [4, 5]                                             # Replacement/insertion
print(L)

L[1:1] = [6, 7]                                             # Insertion(replaces nothing)
print(L)

L[1:2] = []                                                 # Deletion(inserts nothing)
print(L)

# sort of in-place concatenation
L = [1]
print(L)

L[:0] = [2, 3, 4]                                           # Insert all at :0, an empty slice at front
print(L)

L[len(L):] = [5, 6, 7]                                      # Insert all at len(L):, an empty slice at end 
print(L)

L.extend([8, 9, 10])                                        # Insert all at end, named method
print(L)
