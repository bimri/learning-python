D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))
print(list(D.keys()))


# get method returns a default value—None, 
# or a passed-in default—if the key doesn’t exist
print(D.get('spam'))                                    # A key that is there
print(D.get('toast'))                                   # A key that is missing
print(D.get('toast', 88))


# update --> merges k,v of one dict into another
# blindly overwriting values of the same key if there's a clash
print(D)

D2 = {'toast':4, 'muffin':5}
D.update(D2)
print(D)


# pop method deletes the key of the dict & returns its value
print(D)

print(D.pop('muffin'))                                           # Delete and return from a key
print(D.pop('toast'))
print(D)

# pop a list by position
L = ['aa', 'bb', 'cc', 'dd']
L.pop()                         # Delete and return from the end
print(L)

L.pop(1)
print(L)
