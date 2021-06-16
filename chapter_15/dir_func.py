'''the built-in dir function is an easy way to grab a list of all the
attributes available inside an object'''

import sys

print(
    dir(sys)
)

print(
    len(dir(sys))                                           # Number names in sys
)

print(
    len([x for x in dir(sys) if not x.startswith('__')])    # Non __X names only
)

print(
    len([x for x in dir(sys) if not x[0] == '_'])           # Non underscore names
)


# find out what attributes are provided in objects of built-in types
print(
    dir([])
)

print(
    dir("")
)


# operator overloading methods
print(
    len(dir([])), len([x for x in dir([]) if not x.startswith('__')])
)

print(
    len(dir('')), len([x for x in dir('') if not x.startswith('__')])
)


# to filter out double-underscored items that are not of common program interest
print(
    [a for a in dir(list) if not a.startswith('__')]
)

print(
    [a for a in dir(dict) if not a.startswith('__')]
)


# importable and reusable function
def dir1(x):
    return [a for a in dir(x) if not a.startswith('__')]


print(
    dir1(tuple), 
    dir1(set)
)


# Same result, type name or literal
print(
    dir(str) == dir('')
)

print(
    dir(list) == dir([])
)


'''
function serves as a sort of memory-jogger dir'''