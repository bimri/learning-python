"Reduce function lives in functools module"
# Accepts aan iterable to process, but it's bot an iterable itself
# - it returns a single result.

from functools import reduce                            # Import in 3.X

# reduce passes the current sum or product. respectively
print(
    reduce((lambda x, y: x + y), [1, 2, 3, 4])
)

print(
    reduce((lambda x, y: x * y), [1, 2, 3, 4])
)

# for loop equivalent of first case
L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x

print(res)


"Custom own version of reduce"
def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(
    myreduce((lambda x, y: x + y), [1,2,3,4,5])
)

print(
    myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
)


'''
The built-in reduce also allows an optional third argument placed before the items in
the sequence to serve as a default result when the sequence is empty
'''


'''
operator module, which provides functions that correspond to builtin
expressions and so comes in handy for some uses of functional tools
'''
import operator, functools
print(
    functools.reduce(operator.add, [2, 4, 6])       # function-based+
)

print(
    functools.reduce((lambda x, y: x + y), [2, 4, 6])
)
