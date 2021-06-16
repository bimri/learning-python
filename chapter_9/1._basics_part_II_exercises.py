''' 1. The Basics'''
print(2 ** 16)                                          # 2 raised to the power 16
print(2/5, 2/5.0)                                       # Integer / truncates in 2.X, but not 3.X

# Strings

print('spam' + 'eggs')                                  # Concatenation
S = 'ham'
print("eggs " + S)
print(S * 5)                                            # Repetition
S[:0]                                                   # slicing
print(S)


print("green %s and %s" % ("eggs", S))                  # formatting
print('green {0} and {1}'.format('eggs', S))


#Tuples

print(('x',)[0])                                            # Indexing a single-item tuple
print(('x', 'y')[1])                                        # Indexing a two-item tuples


# Lists

L = [1,2,3] + [4,5,6]                                       # List operations
print(L, L[:], L[:0], L[-2], L[-2:])                        
print(([1,2,3] + [4,5,6])[2:4])
print(L)
print([L[2], L[3:]])                                        # Fetch from offsets; store in a list          
L.reverse(); print(L)                                       # Method: reverse list in place 
L.sort(); print(L)                                          # Method: sort list in place
print(L.index(4))                                           # Method: offset of first four (search)


# Dictionaries
print({'a':1, 'b':2}['b'])                                      # Index a dictionary by key 
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0                                                      # Create a new entry
print(D['x'] + D['w'])
D[(1,2,3)] = 4                                                  # A tuple used as a key (immutable)
print(D)
print(list(D.keys()), list(D.values()), (1,2,3) in D)           # Methods, key test


# Empties

print([[]], ["", [], (), {}, None])                             # Lots of nothings: empty objects
