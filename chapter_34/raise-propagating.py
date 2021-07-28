"Propagating Exceptions with raise"
try:
    raise IndexError('spam')                    # Exception remember arguments 
except IndexError:
    print('propagating') 
    raise                                       # Reraise most recent exception


'''
Running a raise this way reraises the exception and propagates it to a higher handler
(or the default handler at the top, which stops the program with a standard error message).
Notice how the argument we passed to the exception class shows up in the error
messages.
'''
