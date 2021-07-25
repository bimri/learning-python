"Example: Default Behavior"
'''
Because the control flow through a program is easier to capture in Python than in
English, let’s run some examples that further illustrate exception basics in the context
of larger code samples in files. 
'''
def gobad(x, y):
    return x / y 

def gosouth(x):
    print(gobad(x, 0)) 

gosouth(1)


""" 
When ran this in a shell window with Python 3.X. The message consists of a stack trace
(“Traceback”) and the name of and details about the exception that was raised. The
stack trace lists all lines active when the exception occurred, from oldest to newest. 
""" 
 

""" 
Because Python detects and reports all errors at runtime by raising exceptions, exceptions
are intimately bound up with the ideas of error handling and debugging in general.
""" 
