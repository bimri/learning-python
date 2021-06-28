'''
In some applications, it’s possible to minimize coding requirements for user-defined iterables
by combining the __iter__ method we’re exploring here and the yield generator
function statement. Because generator functions automatically
save local variable state and create required iterator methods, they fit this role
well, and complement the state retention and other utility we get from classes.

When called, it returns a new generator object with automatic retention
of local scope and code position, an automatically created __iter__ method
that simply returns itself, and an automatically created __next__ method (next in 2.X)
that starts the function or resumes it where it last left off:

generator functions coded as methods in classes have access to saved state in both instance at
tributes and local scope variables.
'''
def gen(x):
    for i in range(x): yield i ** 2


if __name__ == '__main__':
    G = gen(5)                                                         # Create a generator with __iter__ and __next__
    print(G.__iter__() == G)                                                 # Both methods exist on the same object

    I = iter(G)                                                         # Runs __iter__: generator returns itself
    print(next(I), next(I))                                             # Runs __next__
    
    print(list(gen(5)))                                                # Iteration contexts automatically run iter and next
