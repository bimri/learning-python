"""
Where the program goes when an exception is raised depends entirely
upon where it has been—it’s a function of the runtime flow of control through the script,
not just its syntax. The propagation of an exception essentially proceeds backward
through time to try statements that have been entered but not yet exited. This propagation
stops as soon as control is unwound to a matching except clause, but not as it
passes through finally clauses on the way.
""" 

"Example: Control-Flow Nesting"
def action2():
    print(1 + [])                       # Generate TypeError 

def action1():
    try:
        action2()
    except TypeError:                   # Most recent matching try
        print('inner try') 
    
try:
    action1() 
except TypeError:                       # Here, only if action1 re-raises 
    print('outer try') 


'''
Notice, though, that the top-level module code at the bottom of the file wraps a call to
action1 in a try handler, too. When action2 triggers the TypeError exception, there will
be two active try statements—the one in action1, and the one at the top level of the
module file. Python picks and runs just the most recent try with a matching except—
which in this case is the try inside action1.

Again, the place where an exception winds up jumping to depends on the control flow
through the program at runtime. Because of this, to know where you will go, you need
to know where you’ve been. In this case, where exceptions are handled is more a function
of control flow than of statement syntax. However, we can also nest exception
handlers syntactically—an equivalent case we turn to next.
'''

"Example: Syntactic Nesting"
try: 
    try:
        action2() 
    except TabError:                    # Most recent matching try
        print('innter try') 
except TypeError:                       # Here, only if nested handler re-raises 
    print('outer try')


""" 
nested finally handlers all fire on an exception,
whether they are nested syntactically or by means of the runtime flow through physically
separated parts of your code:
"""
try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM') 
