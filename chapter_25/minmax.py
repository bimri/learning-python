"Unit Tests with __name__"

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))                   # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))


'''
This script includes self-test code at the bottom, so we can test it without having to
retype everything at the interactive command line each time we run it.

The problem with the way it is currently coded, however, is that the output of the self-test call will
appear every time this file is imported from another file to be used as a tool—not exactly
a user-friendly feature! To improve it, we can wrap up the self-test call in a __name__
check, so that it will be launched only when the file is run as a top-level script, not when
it is imported: - minmax2.py
'''
