'''
Python 3.3 introduces extended syntax for the yield statement that allows delegation
to a subgenerator with a from generator clause.

'''
"the list here in the following forces the generator to produce all its values"
def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i                        # the comprehension in parentheses is a generator expression

print(
    list(both(5))
)

# new 3.3 syntax
def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(
    list(both(5))
)


print(
    ' : '.join(str(i) for i in both(5))
)


'''
In more advanced roles, however, this extension allows subgenerators to receive sent
and thrown values directly from the calling scope, and return a final value to the outer
generator. The net effect is to allow such generators to be split into multiple subgenerators
much as a single function can be split into multiple subfunctions.
'''