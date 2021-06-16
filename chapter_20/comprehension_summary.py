[x * x for x in range(10)]                              # List comprehension: builds list
                                                        # Like list(generator expr)


(x * x for x in range(10))                              # Generator expression: produces items
                                                        # Parens are often optional


{x * x for x in range(10)}                              # Set comprehension, 3.X and 2.7                                                    
                                                        # {x, y} is a set in these versions too


{x: x * x for x in range(10)}                           # Dictionary comprehension, 3.X and 2.7                                                    



"Scopes and Comprehension Variables"
'''
Python 3.X localizes
loop variables in all four forms—temporary loop variable names in generator, set, dictionary,
and list comprehensions are local to the expression.
'''
X = 99
print([X for X in range(5)])                            # 3.X: generator, set, dict, and list localize

Y = 99
for Y in range(5): pass                                 # But loop statements do not localize names
print(Y)


'''
3.X variables assigned in a comprehension are really a
further nested special-case scope;
'''
X = 'aaa'

def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))                    # Z comprehension, Y local, X global

func()


"Generator, set, and dictionary forms localize names as in 3.X:"
X = 99

print([X for X in range(5)])
print(X)

Y = 99
for Y in range(5): pass                                 # for loops do not localize names in 2.X or 3.X
print(Y)

'''
use unique names for variables in comprehension 
expressions as a rule of thumb.
'''


"Comprehending Set and Dictionary Comprehensions"
'''
set and dictionary comprehensions are just syntactic sugar for passing generator
expressions to the type names. Because both accept any iterable, a generator
works well here:
'''
{x * x for x in range(10)}                              # Comprehension
set(x * x for x in range(10))                           # Generator and type name

{x: x * x for x in range(10)}
dict((x, x * x) for x in range(10))
# print(x)

# Set comprehension equivalent
res = set()
for x in range(10):
    res.add(x * x)

print(res)

# Dict comprehension equivalent
res = {}
for x in range(10):
    res[x] = x * x

print(res)

# print(x)                                                  # Localized in comprehension expressions, but not in loop statements

'''
Notice that although both set and dictionary comprehensions accept and scan iterables,
they have no notion of generating results on demand—both forms build complete objects all at once.
'''



"Extended Comprehension Syntax for Sets and Dictionaries"
# both set and dictionary comprehensions support nested 
# associated clauses to filter items out of the result if
[x * x for x in range(10) if x % 2 == 0]                    # Lists are ordered
{x * x for x in range(10) if x % 2 == 0}                    # But sets are not
{x: x * x for x in range(10) if x % 2 == 0}                 # Neither are dict keys

'''
Nested for loops work as well, though the unordered and no-duplicates nature of both
types of objects can make the results a bit less straightforward to decipher:
'''
[x + y for x in [1, 2, 3] for y in [4, 5, 6]]               # Lists keep duplicates
{x + y for x in [1, 2, 3] for y in [4, 5, 6]}               # But sets do not
{x: y for x in [1, 2, 3] for y in [4, 5, 6]}                # Neither do dict keys

'''
Like list comprehensions, the set and dictionary varieties can also iterate over any type
of iterable—lists, strings, files, ranges, and anything else that supports the iteration
protocol:
'''
{x + y for x in 'ab' for y in 'cd'}
{x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
{k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
{k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
