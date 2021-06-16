"Generator Functions"
# A function def statement that contains a 
# yield statement is turned into a generator
'When called, it returns a new generator object with'
'automatic retention of local scope & code position.'
# with an automatically created __iter__ method 
# that simply returns itself
# and an automatically created __next__ method that
# starts the function or resumes it where it last 
# left off, and raises StopIteration when finished 
# producing results


"Generator expressions"
# A comprehension expression enclosed in parentheses 
# is known as a generator expression.
'When run, it returns a new generator object with the'
'same automically created method interface & state'
"retention as a generator function call's results"
# with an automatically created __iter__ method 
# that simply returns itself
# and an automatically created __next__ method that
# starts the function or resumes it where it last 
# left off, and raises StopIteration when finished 
# producing results

G = (c * 4 for c in 'BIMRI')                                # Generator expression
print(
    list(G)                                                 # Force generator to produce all results
)


# Equivalent generator function
def timesfour(S):                                           # Generator function
    for c in S:
        yield c * 4
    
G = timesfour('KEMET')
print(
    list(G)                                                 # Iterate automatically
)

"Both expressions and functions support both automatic and manual iteration"
G = (c * 4 for c in 'SPAM')
I = iter(G)
# Iterate manually (expression)
print(
    next(I),
    next(I)
)

G = timesfour('spam')
I = iter(G)
# Iterate manually (function)
print(
    next(I),
    next(I)
)

# true statement-based equivalent of expression for gen_expreesion_vs_filter.py section
line = 'aa bbb c'

print(
    ''.join(x.upper() for x in line.split() if len(x) > 1)          # Expression
)

def gensub(line):                                                   # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()
        
print(
    ''.join(gensub(line))                                           # But why generate?
)

'''
cases like this above the use of generators over the
simple statement equivalent shown earlier may be difficult to justify, except on stylistic
grounds
'''


"Generators are one-shot iterators"
