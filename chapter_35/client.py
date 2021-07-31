"Why Exception Hierarchies?"

import mathlib

try:
    mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
    ... # handle and recover...


# Catch everything here (or catch Exception super)
try:
    mathlib.func(...)
except:
    ... # handle and recover...


'''
As a rule of thumb, it’s usually better to be specific 
than general in exception handlers
'''


""" 
Class exception hierarchies fix this dilemma completely. Rather
than defining your library’s exceptions as a set of autonomous classes, arrange them
into a class tree with a common superclass to encompass the entire category: 
""" 
# users of your library simply need to list the common superclass
try:
    mathlib.func(...)
except mathlib.NumErr:
    ... # report and recover...


"""" 
Class exceptions provide a better answer to maintenance issues than strings could.
Class-based exception hierarchies also support state retention and inheritance in ways
that make them ideal in larger programs.
"""
