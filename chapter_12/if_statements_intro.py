# General Format
'''
if test1:                   # if test
    statements1             # associated block
elif test2:                 # optional elifs
    statement2
else:                       # optional else
    statement3
'''

# Basic Examples
if 1:                                       # is Boolean true
    print('true')


if not 1:
    print('true')
else:
    print('false')


'''Multiway Branching'''
x = 'killer rabbit'
if x == 'roger':
    print("shave and a haircut")
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')

# A dictionary-based 'switch'
choice = 'ham'
print({'spam': 1.25,
       'ham': 1.99,                     # Use has_key or get for default
       'eggs': 0.99,
       'bacon': 1.10}[choice])

# The equivalent if statement
if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')


'''Handling switch defaults'''
# get method calls
branch = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}

print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))

# in membership test 
choice = 'bacon'
if choice in branch:
    print(branch[choice])
else: 
    print('Bad Choice')

# try statement
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')


'''Handling larger actions'''
# A table of callable function objects
def function(): pass
def default(): pass

branch = {
    'spam': lambda: ...,
    'ham': function,
    'eggs': lambda: ...,
}

branch.get(choice, default)()                           # called by adding parentheses to trigger their actions

