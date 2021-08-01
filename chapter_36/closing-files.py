"Closing Files and Server Connections"
'''
Exception processing tools are also commonly used to ensure that system resources are
finalized, regardless of whether an error occurs during processing or not.

Some servers require connections to be closed in order to terminate a session
Output files may require close calls to flush their buffers to disk for
waiting consumers, and input files may consume file descriptors if not closed;

File objects are automatically closed when garbage-collected if still open, in some Pythons
it may be difficult to be sure when that will occur.
'''
# myfile = open(r'E:\practice\relative_path', 'w') 
# try:
#     ...process myfile... 
# finally:
#     myfile.close() 

"""
providing context managers that terminate or close the objects for us automatically
when run by the with/as statement:

Compared to the traditional try/finally, context managers are more implicit, which runs contrary
to Python’s general design philosophy. Context managers are also arguably less general
—they are available only for select objects, and writing user-defined context managers
to handle general termination requirements is more complex than coding a try/finally.

On the other hand, using existing context managers requires less code than using try/
finally, as shown by the preceding examples. Moreover, the context manager protocol
supports entry actions in addition to exit actions. In fact, it can save a line of code when
no exceptions are expected at all.
"""
# with open(r'E:\practice\relative_path', 'w') as myfile:
#     ...process myfile...


# myfile = open(filename, 'w') # Traditional form
# ...process myfile...
# myfile.close()

# with open(filename) as myfile: # Context manager form
# ...process myfile...

""" 
Still, the implicit exception processing of with makes it more directly comparable to
the explicit exception handling of try/finally. Although try/finally is the more widely
applicable technique, context managers may be preferable where they are already
available, or where their extra complexity is warranted.
"""
