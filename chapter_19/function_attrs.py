'''
Python’s own implementation-related data stored on functions follows naming conventions
that prevent them from clashing with the more arbitrary attribute names you
might assign yourself
'''

def f(): pass 

print(dir(f))
print(len(dir(f)))
