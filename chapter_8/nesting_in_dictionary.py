# Hypothetical person
rec = {}
rec['name'] = 'Bimri'
rec['age'] = 4000
rec['job'] = 'developer/manager'

print(rec)
print(rec['name'])


''' When nested Python's built-in data types allows
    us to easily represent structured information.'''
rec = {
    'name': 'Bimri',
    'jobs': ['developer', 'manager'],
    'web': 'www.bimri.org',
    'home': {'country': 'Kenya', 'zip': 12579}
}

print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])
print(rec)

# Other ways to make dicts
'''handy if you can spell out 
    the entire dictionary ahead of time'''

{'name': 'Bimri', 'age': 40}                        # Traditional literal expression

'''reate the dictionary one field at a 
    time on the fly'''

D = {}                                              # Assign by keys dynamically
D['name'] = 'Bimri'
D['age'] = 40


'''requires all keys to be strings'''

dict(name='Bimri', age=40)                          # dict keyword argument form


'''useful if you need to build up keys 
and values as sequences at runtime'''

dict([('name', 'Bob'), ('age', 40)])                # dict key/value tuples form

# commonly used in conjunction with the zip function
# dict(zip(keyslist, valueslist))                     # Zipped key/value tuples form


# Zip, Provided all the key’s values are the same initially
print(dict.fromkeys(['a', 'b'], 0))

