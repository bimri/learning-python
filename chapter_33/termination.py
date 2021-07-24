"Termination Actions"
'''
Finally, try statements can say “finally”—that is, they may include finally blocks.
These look like except handlers for exceptions, but the try/finally combination specifies
termination actions that always execute “on the way out,” regardless of whether
an exception occurs in the try block or not;
'''
def fetcher(obj, index): 
    return obj[index]

x = 'bimri'
print(x)

try:
    fetcher(x, 4)
finally:                                                    # Termination actions
    print('after fetch') 


""" 
Here, if the try block finishes without an exception, the finally block will run, and
the program will resume after the entire try.
""" 
fetcher(x, 3)
print('after fetch')


""" 
There is a problem with coding this way, though: if the function call raises an exception,
the print will never be reached. The try/finally combination avoids this pitfall—when
an exception does occur in a try block, finally blocks are executed while the program
is being unwound: 
""" 
def after():
    try:
        fetcher(x, 6)
    finally:
        print('after fetch')
    print('after try?') 


# after()


""" 
Here, we don’t get the “after try?” message because control does not resume after the
try/finally block when an exception occurs. Instead, Python jumps back to run the
finally action, and then propagates the exception up to a prior handler (in this case,
to the default handler at the top). If we change the call inside this function so as not to
trigger an exception, the finally code still runs, but the program continues after the try: 
""" 
def after():
    try:
        fetcher(x, 6)
    finally:
        print('after fetch')
    print('after try?')

# after()


"""
In practice, try/except combinations are useful for catching and recovering from exceptions,
and try/finally combinations come in handy to guarantee that termination
actions will fire regardless of any exceptions that may occur in the try block’s code.

For instance, you might use try/except to catch errors raised by code that you import
from a third-party library, and try/finally to ensure that calls to close files or terminate
server connections are always run.

The with/as statement runs an object’s
context management logic to guarantee that termination actions occur, irrespective of
any exceptions in its nested block:
    >>> with open('lumberjack.txt', 'w') as file: # Always close file on exit
            file.write('The larch!\n')


Although this option requires fewer lines of code, it’s applicable only when processing
certain object types, so try/finally is a more general termination structure, and is often
simpler than coding a class in cases where with is not already supported. On the other
hand, with/as may also run startup actions too, and supports user-defined context
management code with access to Python’s full OOP toolset.            
"""
