"Timing Calls"
'''
decorator times calls made to a decorated function—both
the time for one call, and the total time among all calls. The decorator is applied to two
functions, in order to compare the relative speed of list comprehensions and the map
built-in call:
'''
import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func    = func
        self.alltime =  0
    def __call__(self, *args, **kargs):
        start   = time.perf_counter()
        result  = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


if __name__ == "__main__":
    result = listcomp(5)                                    # Timde for this call, all calls, return value
    listcomp(50000)
    listcomp(500000)
    listcomp(1000000)
    print(result)
    print('allTime= %s' % listcomp.alltime)                 # Total time for all listcomp calls

    print('')
    result = mapcall(5)
    mapcall(50000)
    mapcall(500000)
    mapcall(1000000)
    print(result)
    print('allTime = %s' % mapcall.alltime)                 # Total time for all mapcall calls

    print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


'''
As usual, map calls are almost twice as slow as list
comprehensions when the latter can avoid a function call 
(or equivalently, its requirement of function calls can make map slower).
'''


'Decorators versus per-call timing'
'''
    >>> def listcomp(N): [x * 2 for x in range(N)]
    
    >>> import timer                                    # Chapter 21 techniques
    >>> timer.total(1, listcomp, 1000000)
    (0.1461295268088542, None)
    
    >>> import timeit
    >>> timeit.timeit(number=1, stmt=lambda: listcomp(1000000))
    0.14964829430189397

a nondecorator approach would allow the subject functions to be
used with or without timing, but it would also complicate the call signature when timing
is desired

In general, decorators may be preferred when functions are already deployed as part of
a larger system, and may not be easily passed to analysis functions at calls. On the other
hand, because decorators charge each call to a function with augmentation logic, a
nondecorator approach may be better if you wish to augment calls more selectively.
'''
