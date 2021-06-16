X = set('bimri')
Y = {'i', 'm', 'r', 'ii'}

print(X, Y)                     # A tuple of two sets without parantheses

print(X & Y)                    # Intersection
print(X | Y)                    # Union
print(X - Y)                    # Difference
print(X > Y)                    # Superset

# Preferrable use cases for sets
print(list(set([1,2,1,3,1])))           # Filtering out duplicates(possibly reordered)
print(set('spam') - set('ham'))         # Finding differences in collections
print(set('spam') == set('asmp'))       # Order-neutral equality tests(== is False)


# in membership tests
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])
