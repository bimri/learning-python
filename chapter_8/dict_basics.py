D = {'spam': 2, 'ham': 1, 'eggs': 3}                       # Make a dictionary
print(D['spam'])                                           # Fetch a value by key

print(D)                                                   # Order is "scrambled"
print(len(D))                                              # Number of entries in dictionary
print('ham' in D)                                          # Key membership test alternative
print(list(D.keys()))                                      # Create a new list of D's keys


'Changing Dictionaries in Place'
print(D)
D['ham'] = ['grill', 'bake', 'fry']                        # Change entry (value=list)
print(D)

del D['eggs']                                               # Delete entry
print(D)

D['brunch'] = 'Bacon'                                       # Add new entry
print(D)
