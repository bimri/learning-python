# List-based "record"
L = ['Bob', 40.5, ['dev', 'mgr']]
print(L[0])
print(L[1])
print(L[2][1])

# Dictionary-based "record"
D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
print(D['name'])
print(D['age'])
print(D['jobs'][1])

# same record recoded with keywords
D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(D['name'])
D['jobs'].remove('mgr')
print(D)


'''
    Sets:
        - are much like the keys of a valueless dictionary;
        - they don’t map keys to values;
        - can often be used like dictionaries for fast lookups when there is no associated value
'''
D = {}
D['state1'] = True                                  # A visited-state dictionary
print('state1' in D)
print(D)

# Set
S = set()
S.add('state1')                                     # Same, but with sets
print('state1' in S)
