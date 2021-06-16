# Open pairs may span lines - works for anything in curly braces, parentheses
L = ["Good",
     "Bad",
     "Ugly"]

# backslashes to continue lines
a = b = c = d = e = f = g = 0
if a == b and c == d and \
    d == e and f == g:
    print('olde')


# But parentheses usually do too, and are obvious
if (a == b and c == d and
    d == e and f == g):
    print('new')


# More than one simple statement
x = 1; y = 2; print(x)


# comments inclided here
S = """
aaaa            
bbbb                # include comments
cccc"""

# Comments here are ignored
s = ('aaaa'
'bbbb'                                                  # Comments here are ignored
'cccc')

print(S)
print(s)


# move a compound statement’s body up to the header line
if 1: print('hello moved to the header line')
