"Exception Idioms"
'Breaking Out of Multiple Nested Loops: “go to”'

'''
Exceptions provide a more structured option that localizes
the jump to a specific block of nested code.

Python’s break statement exits just the single closest enclosing loop, but
we can always use exceptions to break out of more than one loop level if needed:
'''

class Exitloop(Exception): pass 

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop                    # break exits just one level
                print('loop3: %s' % i) 
            print('loop2') 
        print('loop1') 
except Exitloop:
    print('continuing')                                     # Or just pass, to move on 


""" 
Also notice that variable i is still what it was after the try statement exits. Variable
assignments made in a try are not undone in general, though as we’ve seen, exception
instance variables listed in except clause headers are localized to that clause, and the
local variables of any functions that are exited as a result of a raise are discarded.
Technically, active functions’ local variables are popped off the call stack and the objects
they reference may be garbage-collected as a result, but this is an automatic step.
""" 


"Exceptions Aren’t Always Errors"
'In Python, all errors are exceptions, but not all exceptions are errors.'
while True:
    try:
        line = input()                                          # Read line from stdin(raw_input in 2.X)
    except EOFError:
        break                                                   # Exit loop at end-of-file
    else:
        ... # process next line here ...

'''
Several other built-in exceptions are similarly signals, not errors—for example, calling
sys.exit() and pressing Ctrl-C on your keyboard raise SystemExit and KeyboardInter
rupt, respectively.
'''
