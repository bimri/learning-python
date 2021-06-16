'''
many Python standard library tools generate values
today too, including email parsers, and the standard directory walker—which at each
level of a tree yields a tuple of the current directory, its subdirectories, and its files:
'''
import os
for (root, subs, files) in os.walk('.'):                            # Directory walk generator
    for name in files:                                              # A python 'find' operation
        if name.startswith('gen'):
            print(root, name)

G = os.walk(r'E:\practice\learning_python')

# Single-scan iterator: iter(G) optional
print(iter(G) is G)

I = iter(G)
print(next(I))
print(next(I))
print(next(I))
print(next(I))

"By yielding results as it goes, the walker does not require its clients to wait for an entire tree to be scanned."
