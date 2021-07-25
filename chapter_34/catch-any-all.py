"Catching any and all exceptions"
''' 
• except clauses that list no exception name (except:) catch all exceptions not previously
listed in the try statement.
• except clauses that list a set of exceptions in parentheses (except (e1, e2, e3):)
catch any of the listed exceptions.

Because Python looks for a match within a given try by inspecting the except clauses
from top to bottom, the parenthesized version has the same effect as listing each exception
in its own except clause, but you have to code the statement body associated
with each only once.
'''
def action():
    pass


try:
    action() 
except NameError:
    ...
except IndexError:
    ...
except KeyError:
    ...
except (AttributeError, TypeError, SyntaxError):
    ...
else:
    ...


""" 
In this example, if an exception is raised while the call to the action function is running,
Python returns to the try and searches for the first except that names the exception
raised. It inspects the except clauses from top to bottom and left to right, and runs the
statements under the first one that matches. If none match, the exception is propagated
past this try. Note that the else runs only when no exception occurs in action—it does
not run when an exception without a matching except is raised.
""" 
