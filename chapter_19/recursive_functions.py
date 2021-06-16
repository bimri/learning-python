"recursive functions call themselves- (in)directly"
'they allow programs to traverse structures that have'
'abitrary and unpredictable shapes and depths'
"e.g. planning travel routes, analyzing langiage & crawling links on the Web"

# Recursion is even an alternative to simple loops and iterations
# though not the simplest or most efficient one.

"Summation with Recursion"
# sum a list(or other sequence) of numbers
def mysum(L):
    print(L)                                                # Trace recursive levels
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])                          # call myself recursively

# print(mysum([1, 2, 3, 4, 5]))                             # use terminal


"Coding Alternatives" 
# if/else ternary expression
def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:])             # Use ternary expression

def mysum2(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])     # Any type, assume one

def mysum3(L):              # works on arbitrary iterables
    first, *rest = L
    return first if not rest else first + mysum3(rest)      # Use ext seq assign

'''
latter two of these fail for empty lists but allow for sequences of any object type
that supports +, not just numbers
'''

# Type interactively
mysum1([1])                                                  # mysum([]) fails in last 2
mysum2([1, 2, 3, 4, 5])
mysum3(('s', 'p', 'a', 'm'))                                 # But various types now work
mysum3(['spam', 'ham', 'eggs'])


"Recursion can be direct or indirect"
def mysum4(L):
    if not L: return 0
    return nonempty(L)                                      # Call a function that calls me

def nonempty(L):
    return L[0] + mysum4(L[1:])                             # Indirectly recursive

# Type interactively
mysum4([1.2, 3.4, 5.6, 6.8])
