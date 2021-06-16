from collections import namedtuple                              # import extension type

bob = ('Bob', 40.5, ['dev', 'mgr'])                             # Tuple record
print(bob)

print(bob[0], bob[2])                                           # Access by position


# convert parts of the dictionary to a tuple
bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])           # Dictionary record

print(tuple(bob.values()))                                      # Values to tuple
print(list(bob.items()))                                        # Items to tuple list


''' 
    Namedtuple: -
        -> objects that offer both positional and named access to record fields.
        -> named tuples are a tuple/class/dictionary hybrid
        -> named tuples build new classes that extend the tuple type, inserting 
           a property accessor method for each named field that maps the name to its position.
'''
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])                # Make a generated class

bimri = Rec('Bimri', age=4000, jobs=['dev', 'mgr'])             # A named-tuple record
print(bimri)
print(bimri[0], bimri[2])                       # access by position
print(bimri.name, bimri.jobs)                   # access by attribute


# Converting to a dictionary supports key-based behavior
O = bimri._asdict()                             # Dictionary-like form
print(O['name'], O['jobs'])                     # Access by key too

print(O)


# both tuples and named tuples support unpacking tuple assignment
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
name, age, jobs = bob                               # Tuple assignment
print(name, jobs)

for x in bob: print(x)                              # Iteration context

# Dict equivalent (but order may vary)
bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()
print(name, job)


# Step though keys, index values
for x in bob: print(bob[x])

# Step through values view
for x in bob.values(): print(x)
