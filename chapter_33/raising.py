"Raising Exceptions"
# exceptions can be raised by Python or by your program, and can be caught or not
'to trigger an exception manually, simpy run a raise statement'
'user-generated exceptions are caught the same way as those Python raises'

try: 
    raise IndexError
except IndexError:                                          # Trigger exception manually
    print('An IndexError occurred')


""" 
As usual, if they’re not caught, user-triggered exceptions are propagated up to the toplevel
default exception handler and terminate the program with a standard error message:
""" 
# raise IndexError


""" 
the assert statement can be used to trigger exceptions,
too—it’s a conditional raise, used mostly for debugging purposes during development:
""" 
assert False, 'Nobody expects the Spanish Inquisition!'
