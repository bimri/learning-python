"""
1. Method decorators: As mentioned in one of this chapter’s notes, the timerdeco2.
py module’s timer function decorator with decorator arguments that we
wrote in the section “Adding Decorator Arguments” on page 1298 can be applied
only to simple functions, because it uses a nested class with a __call__ operator
overloading method to catch calls. This structure does not work for a class’s methods
because the decorator instance is passed to self, not the subject class instance.
Rewrite this decorator so that it can be applied to both simple functions and methods
in classes, and test it on both functions and methods. (Hint: see the section
“Class Blunders I: Decorating Methods” on page 1289 for pointers.) Note that you
will probably need to use function object attributes to keep track of total time, since
you won’t have a nested class for state retention and can’t access nonlocals from
outside the decorator code. As an added bonus, this makes your decorator usable
on both Python 3.X and 2.X.
"""
# Call timer decorator for both functions and methods.
# Use decorator arguments to pass in total time.
 
import time

def timer(label='', trace=True):                                # On decotator args: retain args
    def onDecorator(func):                                      # On @: retain decorated func
        def onCall(*args, **kargs):                             # On calls: call original
            start = time.perf_counter()                         # State: in closure
            result = func(*args, **kargs)                       # Call: capture return time  
            elapsed = time.perf_counter() - start               # State: in global scope
            onCall.alltime += elapsed                           # State: in onCall
            if trace:                                           # Trace: report
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result                                      # Return: result
        onCall.alltime = 0                                     # State: in global scope
        return onCall
    return onDecorator
