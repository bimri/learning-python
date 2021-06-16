L = ['loyal', '6lack', 'SONG!']
L.append('lying')                                   # Append method call: add item at end
print(L)

L.sort()
print(L)


L = ['abc', 'ABD', 'aBe']
L.sort()                                            # Sort with mixed case
print(L)

L = ['abc', 'ABD', 'aBe']                           # Normalize to lowercase
L.sort(key=str.lower)
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)                 # Change sort order
print(L)

# Sorting built-in
L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))

# Pretransform items: differs!
L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True))


# Reverse, reversed, extend, pop
L = [1, 2]
L.extend([3, 4, 5])                                     # Add many items at teh end(like in-place +)
print(L)

L.pop()                                                 # Delete and return last item(by default: -1)
print(L)

L.reverse()                                             # In-place reversal method
print(L)

print(list(reversed(L)))                                # Reversal build-in with a result(iterator)


'''Last-in-first-out(LIFO) stack structure'''
L = []
L.append(1)                                             # Push onto stack
L.append(2)
print(L)

L.pop()                                                 # Pop off stack
print(L)


# remove, insert, count & index methods
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))                                  # Index of an object (search/find)

L.insert(1, 'toast')                                    # Insert at position
print(L)

L.remove('eggs')                                        # Delete by value
print(L)

print(L.pop(1))                                         # Delete by position
print(L)

print(L.count('spam'))                                  # Number of occurences


# Other list operations
L = ['spam', 'eggs', 'ham', 'toast']
print(L)                                                
del L[0]                                               # Delete one item
print(L)

del L[1:]                                               # Delete an entire section
print(L)
