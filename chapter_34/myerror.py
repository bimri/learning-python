"Example: Coding Termination Actions with try/finally"
class MyError(Exception):
    pass 

def stuff(file):
    raise MyError() 

file = open('data', 'w')                # Open an output file (this can fail too)

try:
    stuff(file)                         # Raises exception
finally:
    file.close()                        # Always close file to flush output buffers
print('not reached')                    # Continue here only if no exception 


'''
When the function in this code raises its exception, the control flow jumps back and
runs the finally block to close the file. The exception is then propagated on to either
another try or the default top-level handler, which prints the standard error message
and shuts down the program. Hence, the statement after this try is never reached. If
the function here did not raise an exception, the program would still execute the
finally block to close the file, but it would then continue below the entire try statement.
'''


""" 
In this specific case, we’ve wrapped a call to a file-processing function in a try with a
finally clause to make sure that the file is always closed, and thus finalized, whether
the function triggers an exception or not. This way, later code can be sure that the file’s
output buffer’s content has been flushed from memory to disk. A similar code structure
can guarantee that server connections are closed, and so on. 
""" 
