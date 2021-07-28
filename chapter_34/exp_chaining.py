"Python 3.X Exception Chaining: raise from"
'''
Exceptions can sometimes be triggered in response to other exceptions—both deliberately
and by new program errors.

Python 3.X allows raise statements to have an optional from clause:
    raise newexception from otherexception
'''

try:
    1/0
except Exception as E:
    raise TypeError('Bad') from E                       # Explicitly chained exceptions 
...



""" 
When an exception is raised implicitly by a program error inside an exception handler,
a similar procedure is followed automatically: the previous exception is attached to the
new exception’s __context__ attribute and is again displayed in the standard error
message if the exception goes uncaught:
""" 

try:
    1/0
except:
    badname                                             # Implictly chained exceptions
...


""" 
In both cases, because the original exception objects thus attached to new exception
objects may themselves have attached causes, the causality chain can be arbitrary
long, and is displayed in full in error messages. That is, error messages might give more
than two exceptions. The net effect in both explicit and implicit contexts is to allow
programmers to know all exceptions involved, when one exception triggers another:
""" 

try:
    try:
        raise IndexError() 
    except Exception as E:
        raise TypeError() from E 
except Exception as E:
    raise SyntaxError() from E 


'''
Code like the following would similarly display three exceptions, though implicitly
triggered here:
'''
try:
    try:
        1 / 0 
    except:
        badname
except:
    open('nonesuch')
