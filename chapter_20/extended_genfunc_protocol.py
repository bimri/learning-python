"Send versus next"
# send method advances to the next item in the series of results
# provides a way for the caller to communicate with the generator

def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
print(next(G))                                      # Must call next() first, to start generator

print(
    G.send(77)                                      # Advance, and send value to yield expression
)

print(
    G.send(88)
)

print(
    next(G)
)

'''
The send method can be used, for example, to code a generator that its caller can terminate
by sending a termination code, or redirect by passing a new position in data
being processed inside the generator.
'''

'''
generators in 2.5 and later also support a throw(type) method to raise an
exception inside the generator at the latest yield, and a close method that raises a
special GeneratorExit exception inside the generator to terminate the iteration entirely.
'''

"Also note that Python 3.3 introduces an extension to yield—a from clause—that allows generators to delegate to nested generators"