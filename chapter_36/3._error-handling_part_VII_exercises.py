"""
3. Error handling. Write a function called safe(func, *pargs, **kargs) that runs any
function with any number of positional and/or keyword arguments by using the
* arbitrary arguments header and call syntax, catches any exception raised while
the function runs, and prints the exception using the exc_info call in the sys module.
Then use your safe function to run your oops function from exercise 1 or 2.
Put safe in a module file called exctools.py, and pass it the oops function interactively.
What kind of error messages do you get? Finally, expand safe to also print
a Python stack trace when an error occurs by calling the built-in print_exc function
in the standard traceback module; see earlier in this chapter, and consult the
Python library reference manual for usage details. We could probably code safe as
a function decorator using Chapter 32 techniques, but we’ll have to move on to the
next part of the book to learn fully how (see the solutions for a preview).
"""
import sys, traceback

class MyError(Exception): pass

def oops():
    raise MyError('Spam!')

def safe(callee, *pargs, **kargs):
    try:
        callee(*pargs, **kargs)
    except:
        traceback.print_exc()
        print('Got %s %s' %(sys.exc_info()[0], sys.exc_info()[1]))


if __name__ == '__main__':
    safe(oops)


'''
The following sort of code could turn this into a function decorator that could wrap
and catch exceptions raised by any function
'''
def salama(callee):
    def callproxy(*pargs, **kargs):
        try:
            return callee(*pargs, **kargs) 
        except:
            traceback.print_exc() 
            print('Got %s %s' %(sys.exc_info()[0], sys.exc_info()[1]))
    return callproxy


if __name__ == '__main__':
    @salama
    def test():
        oops()
    
    test()
