# Lambda is commonly used to code jump tables
# which are lists/dicts of actions to be performed on demand

L = [lambda x: x ** 2,                  # Inline function definition
    lambda x: x ** 3,
    lambda x: x ** 4]                   # A list of three callable functions

for f in L:
    print(f(2))                         # Prints 4, 8, 16

print(L[0](3))                          # Prints 9


"Multiway branch switches: The finale"
# actions tables
key = 'got'
{'already': (lambda: 2 + 2),
 'got':     (lambda: 2 * 4),
 'one':     (lambda: 2 ** 6)}[key]()


# def equivalent
def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6

key = 'one'
{'already': f1, 'got': f2, 'one': f3}[key]()


'''
How (Not) to Obfuscate Your Python Code

    if a:
        b
    else:
        c
    

    b if a else c
    ((a and b) or c)
'''

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))
print(lower('aa', 'bb'))


"Loops"
import sys
showall = lambda x: list(map(sys.stdout.write, x))          # 3.X: must use list
t = showall(['spam\n', 'toast\n', 'eggs\n'])                # 3.X: can use print

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

showall = lambda x: [print(line, end='') for line in x]     # Same: 3.X only
showall = lambda x: print(*x, sep='', end='')               # Same: 3.X only
