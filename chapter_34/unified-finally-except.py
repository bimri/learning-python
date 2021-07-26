"Combining finally and except by Nesting"
'''
it is actually possible to combine finally and except clauses in a
try by syntactically nesting a try/except in the try block of a try/finally statement. 
'''
# try:                                # Nested equivalent to merged form
#     try:
#         main-action 
#     except Exception1:
#         handler1
#     except Exception2:
#         handler2
#     ...
#     else:
#         no-error
# finally:
#     cleanup

'''
Again, the finally block is always run on the way out, regardless of what happened in
the main action and regardless of any exception handlers run in the nested try
Mixing finally into the same statement makes your code arguably easier to write and
read, and is a generally preferred technique today.
'''
