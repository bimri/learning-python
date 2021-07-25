"The try/finally Statement"
'''
The other flavor of the try statement is a specialization that has to do with finalization
(a.k.a. termination) actions. If a finally clause is included in a try, Python will always
run its block of statements “on the way out” of the try statement, whether an exception
occurred while the try block was running or not. Its general form is:
'''
try:
    statements                  # Run this action first
finally:
    statements                  # Always run this code on the way out 



""" 
With this variant, Python begins by running the statement block associated with the
try header line as usual. What happens next depends on whether an exception occurs
during the try block:
    • If an exception does not occur while the try block is running, Python continues on
    to run the finally block, and then continues execution past the try statement.

    • If an exception does occur during the try block’s run, Python still comes back and
    runs the finally block, but it then propagates the exception up to a previously
    entered try or the top-level default handler; the program does not resume execution
    below the finally clause’s try statement. That is, the finally block is run even if
    an exception is raised, but unlike an except, the finally does not terminate the
    exception—it continues being raised after the finally block runs. 
""" 


'''
The try/finally form is useful when you want to be completely sure that an action will
happen after some code runs, regardless of the exception behavior of the program.
In practice, it allows you to specify cleanup actions that always must occur, such as file
closes and server disconnects where required.
'''
