"Catching all: The empty except and Exception"
'''
If you really want a general “catchall” clause, an empty except does the trick:
The empty except clause is a sort of wildcard feature—because it catches everything, it
allows your handlers to be as general or specific as you like.
In some scenarios, this form may be more convenient than listing all possible exceptions in a try.
'''

def action():
    pass 


try: 
    action() 
except NameError:
    ...                             # Handle NameError 
except IndexError:
    ...                             # Handle IndexError 
except:
    ...                             # Handle all other exceptions
else: 
    ...                             # Handle the no-exception case 


# wildcard feature
try: 
    action() 
except:
    ...                             # Catch all possible exceptions


'''
Empty excepts also raise some design issues, though. Although convenient, they may
catch unexpected system exceptions unrelated to your code, and they may inadvertently
intercept exceptions meant for another handler.

For example, even system exit calls and Ctrl-C key combinations in Python trigger exceptions, 
and you usually want these to pass. Even worse, the empty except may also catch genuine programming
mistakes for which you probably want to see an error message.
'''


""" 
Python 3.X more strongly supports an alternative that solves one of these problems—
catching an exception named Exception has almost the same effect as an empty
except, but ignores exceptions related to system exits:

This form has most of the same convenience of
the empty except, without the risk of catching exit events. Though better, it also has
some of the same dangers—especially with regard to masking programming errors.
"""
try:
    action() 
except Exception:
    ...                                 # Catch all possbile exceptions, except exists
