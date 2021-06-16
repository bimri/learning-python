'''iteration mini-language'''


# FILETER CLAUSES: IF
lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)

# for loop statement equivalent
res = []
for line in open('script2.py'):                       # takes up four lines instead of one and may run slower
    if line[0] == 'p':
        res.append(line.rstrip())

print(res)

# selects only lines that end in a digit
print(
    [line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()]
)

# gives the total lines in a text file
fname = r'E:\practice\learning_python\chapter_14\listcompre.txt'
print(
    len(open(fname).readlines())                                    # All lines
)

print(
    len([line for line in open(fname) if line.strip() != ''])       # Nonblank lines
)


# NESTED LOOPS: FOR
print(
    [x + y for x in 'abc' for y in 'lmn']                       # builds a list of the concatenation of for every in one x + y...
)

# statement form
res = []
for x in 'xyz':
    for y in '123':
        res.append(x + y)

print(res)

print('\n')

'''every built-in tool that scans from left to right
    across objects uses the iteration protocol
'''
# Use file iterators
for line in open('script2.py'):
    print(line.upper(), end='')

print('\n')

'''
file object’s iterator automatically to scan line by line, fetching an iterator with
__iter__ and calling __next__ each time through
'''
uppers = [line.upper() for line in open('script2.py')]
print(uppers)

# map is itself an iterable in 3.X
print(
    map(str.upper, open('script2.py'))
)
print(
    list(map(str.upper, open('script2.py')))
)

print('\n')


'''Many of Python’s other built-ins process iterables'''
print(
    sorted(open('script2.py')),                             # returns an actual list
sorted
)
print()

print(
    list(zip(open('script2.py'), open('script2.py')))           # zip, enumerate, and filter also return an iterable
)
print()

print(
    list(enumerate(open('script2.py')))
)
print()

print(
    list(filter(bool, open('script2.py')))                      # nonempty=True
)
print()

import functools, operator
print(
    functools.reduce(operator.add, open('script2.py'))          # reduce runs pairs of items in an iterable through a function
)
print()

# string method join
print(
    list(open('script2.py'))
)
print()

print(
    tuple(open('script2.py'))
)
print()

print(
    '&&'.join(open('script2.py'))
)
print()


# TOOLS
a, b, c, d = open('script2.py')                         # Sequence assignment
print(a, d)

a, *b = open('script2.py')                              # 3.X extended form
print(a, b)

print(
    'y = 2\n' in open('script2.py')                     # Membership test
)

print(
    'x = 2\n' in open('script2.py')
)


L = [11, 22, 33, 44]                                    # Slice assignment
L[1:3] = open('script2.py')
print(L)

L = [11]                                                
L.extend(open('script2.py'))                            # list.extend method
print(L)



'''Iteration is a broadly supported and powerful model'''
print(
    set(open('script2.py'))
)

print(
    {line for line in open('script2.py')}
)

print(
    {ix: line for ix in enumerate(open('script2.py'))}
)


# set and dictionary comprehensions support the 
# extended syntax of list comprehensions 
print(
    {line for line in open('script2.py') if line[0] == 'p'}
)

print(
    {ix: line for (ix, line) in enumerate(open('script2.py')) if line[0] == 'p'}
)


# Generator expression - deploys same syntax as comprehensions
# but is also iterable itself
print(
    list(line.upper() for line in open('script2.py'))
)


'''SUM, ANY, ALL, MAX, MIN accept any iterable as an argument & 
use iteration protocol to scan it, but return a single result'''
print(
    sum([3, 2, 3, 4, 5, 0])                                 # sum expects numbers only
)

print(
    any(['spam', '', 'ni'])
)

print(
    all(['spam', '', 'ni'])
)

print(
    max([3, 2, 5, 1, 4])
)

print(
    min([3, 2, 5, 1, 4])
)

# Line with max/min string value
print(
    max(open('script2.py'))
)

print(
    min(open('script2.py'))
)


'''form can be used in function calls *arg
to unpack a collection of values into individual arguments'''
def f(a, b, c, d): print(a, b, c, d, sep='&')

print(f(1,23,3,44))

# unpack into arguments
print(f(*[1, 2, 3, 4]))

print(f(*(open('script2.py'))))


# Zip tuples: returns an iterable
X = (1,2)
Y = (3,4)

print(
    list(zip(X,Y))
)

# Unzip a zip!
A,B = zip(*zip(X,Y))

print(A, B)
