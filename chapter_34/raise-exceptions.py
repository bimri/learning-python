"Raising Exceptions"
'''
the following two forms are equivalent—both raise an instance of the exception class named,
but the first creates the instance implicitly:
'''
raise IndexError                # Class (instance created) 
raise IndexError()              # Instance (created in statement)


''' 
We can also create the instance ahead of time—because the raise statement accepts
any kind of object reference, the following two examples raise IndexError just like the
prior two:
'''
exc = IndexError()              # Create instance ahead of time 
raise exc 

excs = [IndexError, TypeError] 
raise excs[0] 


'''
When an exception is raised, Python sends the raised instance along with the exception.
If a try includes an except name as X: clause, the variable X will be assigned the instance
provided in the raise:

The as is optional in a try handler (if it’s omitted, the instance is simply not assigned
to a name), but including it allows the handler to access both data in the instance and
methods in the exception class.
'''
try:
    ...
except IndexError as X:         # X assigned the raise instance object 
    ...


# model works the same for user-defined exceptions
class MyExc(Exception): pass 
...
raise MyExc('spam')             # Exception class with constructor args 
... 

try:
    ... 
except MyExc as X:              # Instance attributes in handler 
    print(X.args) 


""" 
Regardless of how you name them, exceptions are always identified by class instance
objects, and at most one is active at any given time. Once caught by an except clause
anywhere in the program, an exception dies (i.e., won’t propagate to another try),
unless it’s reraised by another raise statement or error.
""" 
