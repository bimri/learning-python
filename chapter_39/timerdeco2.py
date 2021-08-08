"Adding Decorator Arguments"
import time 

def timer(label='', trace=True):                    # On decorator args:retain args
    class Timer:
        def __init__(self, func):                   # On @: retain decorated func
            self.func    = func
            self.alltime = 0
        def __call__(self, *args, **kargs):         # On calls: call original
            start   = time.perf_counter()
            result  = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer


""" 
Mostly all we’ve done here is embed the original Timer class in an enclosing function,
in order to create a scope that retains the decorator arguments per deployment. The
outer timer function is called before decoration occurs, and it simply returns the
Timer class to serve as the actual decorator. On decoration, an instance of Timer is made
that remembers the decorated function itself, but also has access to the decorator arguments
in the enclosing function scope.
""" 


'Timing with decorator arguments'
if __name__ == '__main__':
    import sys
    from timerdeco2 import timer
    force = list if sys.version_info[0] == 3 else (lambda X: X)

    @timer(label='[CCC]==>')
    def listcomp(N): # Like listcomp = timer(...)(listcomp)
        return [x * 2 for x in range(N)] # listcomp(...) triggers Timer.__call__

    @timer(trace=True, label='[MMM]==>')
    def mapcall(N):
        return force(map((lambda x: x * 2), range(N)))

    for func in (listcomp, mapcall):
        result = func(5) # Time for this call, all calls, return value
        func(50000)
        func(500000)
        func(1000000)
        print(result)
        print('allTime = %s\n' % func.alltime) # Total time for all calls
        
    print('**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


""" 
As usual, we can also test interactively to see how the decorator’s configuration arguments
come into play:
    >>> from timerdeco2 import timer
    >>> @timer(trace=False) # No tracing, collect total time
    ... def listcomp(N):
    ...     return [x * 2 for x in range(N)]
    ...

    >>> x = listcomp(5000)
    >>> x = listcomp(5000)
    >>> x = listcomp(5000)
    >>> listcomp.alltime
    0.0037191417530599152
    >>> listcomp
    <timerdeco2.timer.<locals>.Timer object at 0x02957518>
    
    >>> @timer(trace=True, label='\t=>') # Turn on tracing, custom label
    ... def listcomp(N):
    ... return [x * 2 for x in range(N)]
    ...
    
    >>> x = listcomp(5000)
    => listcomp: 0.00106, 0.00106
    >>> x = listcomp(5000)
    => listcomp: 0.00108, 0.00214
    >>> x = listcomp(5000)
    => listcomp: 0.00107, 0.00321
    >>> listcomp.alltime
    0.003208920466562404
""" 


'''
As is, this timing function decorator can be used for any function, both in modules and
interactively. In other words, it automatically qualifies as a general-purpose tool for
timing code in our scripts.
'''
