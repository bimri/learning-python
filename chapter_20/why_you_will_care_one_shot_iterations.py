'''
WRAPPING calls in map list calls in 3.X is not just for display!!!!!!
'''
def myzip(*args):
    iters = list(map(iter, args))                           # Allow multiple scans
    while iters:                                            # while iters: suffices to loop if at least one argument is passed, and avoids an infinite loop otherwise
        res = [next(i) for i in iters]                      # no reason to catch the StopIteration raised by the next(it) —allowing it to pass ends this generator function and has the same effect that a statement would return
        yield tuple(res)

print(list(myzip('abc', 'lmnop')))
