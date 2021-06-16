#!python
"""
Emulate most of the 3.X print function for use in 2.X (and 3.X).
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""
import sys 

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')                     # keyword arg defaults
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


"Using Keyword-Only Arguments"
# Use 3.X only keyword-only args
def print4(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False 
    file.write(output + end)
