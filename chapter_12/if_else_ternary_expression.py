# which sets A to either Y or Z, based on the truth value of X:
X = 0
Y = 1
Z = 2

if X:
    A = Y
else:
    A = Z

# new expression format
A = Y if X else Z


# Example
# For strings, nonempty means true
A = 't' if 'spam' else 'f'
print(A)

A = 't' if '' else 'f'
print(A)


'''somewhat unusual behavior of Python Boolean operators'''
a = b = c = 0
x = a or b or c or None


# Short-circuit of Boolean operators
def f1():
     pass
def f2(): 
    pass

if f1() or f2(): ...
'''Here, if f1 returns a true (or nonempty) value, Python will never run f2. To guarantee
that both functions will be run, call them before the or:'''
tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...


# Filter call & list compre - evaluate all values 
# and return all that are true
L = [1, 0, 2, 0, 'spam', '', 'ham', []]
f = list(filter(bool, L))                                   # Get true values
print(f)

f = [x for x in L if x]                                     # Comprehensions
print(f)

# Aggregate truth
print(any(L), all(L))
