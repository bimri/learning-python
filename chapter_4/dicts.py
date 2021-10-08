D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D['food'])        # Fetch value of key 'food'
D['quantity'] += 1      # Add 1 to 'quantity' value
print(D)


# Creation techniques for dicts
T = {}
T['name'] = 'Bimri'
T['job']  = 'dev'
T['age']  = 400

print(T)
print(T['name'])


# Keyword usage to create previous dict
bimri1 = dict(name='Bimri', job='dev', age=400)         # Keywords
print(bimri1)

# Usage of ZIP to chain keys list & values list
bimri2 = dict(zip(['name', 'job', 'age'], ['Bimri', 'dev', 400]))
print(bimri2)


# Nesting data
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])

rec['jobs'].append('janitor')
print(rec)


'''
To check for Key is present in a dict collection
use "in" membership test - so as not to encounter
errors - for missing keys
'''
P = {'a': 1, 'b': 2, 'c': 3}
print(P)

P['e'] = 99
print(P)

# Rererencing a nonexistent key is an error
# print(P['f'])       # you'll run into an error

print('f' in P)

if not 'f' in P:
    print('missing')


if not 'f' in P:
    print('missing')
    print('no, really...')


# Sorting keys: for Loops
Y = {'a': 1, 'b': 2, 'c': 3}
print(Y)

Ks = list(Y.keys())             # unordered keys list
print(Ks)                       

Ks.sort()                       # Sorted keys list
print(Ks)

for key in Ks:
    print(key, '=>', Y[key])


# Use sorted - to sort keys automatically
print(Y)

for key in sorted(Y):
    print(key, '--->', Y[key])


for c in 'Nyathi':
    print(c.capitalize())

for x in 'bimri':
    print(x.upper())


# While loop
x = 4
while x > 0:
    print('books!' * x)
    x -= 1
