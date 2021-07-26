"Unified try/except/finally"

# try:                            # Merged form 
#     main-action 
# except Exception1:
#     handler1
# except Exception2:              # Catch exceptions 
#     handler2 
# ...
# else:                           # No-exceptions handler 
#     else-block 
# finally:                        # The finally encloses all else 
#     finally-block 


""" 
The code in this statement’s main-action block is executed first, as usual. If that code
raises an exception, all the except blocks are tested, one after another, looking for a
match to the exception raised. If the exception raised is Exception1, the handler1 block
is executed; if it’s Exception2, handler2 is run, and so on. If no exception is raised, the
else-block is executed. 
""" 


'''
The net effect is that the finally is always run, regardless of whether:
    • An exception occurred in the main action and was handled.
    • An exception occurred in the main action and was not handled.
    • No exceptions occurred in the main action.
    • A new exception was triggered in one of the handlers.

Again, the finally serves to specify cleanup actions that must always occur on the way
out of the try, regardless of what exceptions have been raised or handled.
'''
