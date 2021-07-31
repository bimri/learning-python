"Built-in Exception Classes"
'''
All built-in exceptions that Python itself may raise are predefined class objects.
They are organized into a shallow hierarchy with general superclass categories and 
specific subclass types.

Python organizes the built-in exceptions into a hierarchy,
to support a variety of catching modes.

    - BaseException: topmost root, printing and constructor defaults
    - Exception: root of user-defined exceptions
    - ArithmeticError: root of numeric errors
    - LookupError: root of indexing errors

'''

"Built-in Exception Categories"
# built-in class tree allows you to choose how specific or general your handlers will be.
'''
For example, because the built-in exception ArithmeticError is a superclass for
more specific exceptions such as OverflowError and ZeroDivisionError:
    • By listing ArithmeticError in a try, you will catch any kind of numeric error raised.
    • By listing ZeroDivisionError, you will intercept just that specific type of error, and
      no others.
'''
try:
    action() 
except Exception:                                       # Exits not caught here
    ... # Handle all application exceptions...
else:
    ... # Handle all non-error situations...


try:
    f = open('nonesuch.txt')
except FileNotFoundError:
    print('No such file') 



"Default Printing and State"
'''
Built-in exceptions also provide default print displays and state retention, which is often
as much logic as user-defined classes require. Unless you redefine the constructors your
classes inherit from them, any constructor arguments you pass to these classes are
automatically saved in the instance’s args tuple attribute, and are automatically displayed
when the instance is printed. An empty tuple and display string are used if no
constructor arguments are passed, and a single argument displays as itself (not as a
tuple).

This explains why arguments passed to built-in exception classes show up in error
messages—any constructor arguments are attached to the instance and displayed when
the instance is printed:
    >>> raise IndexError                            # Same as IndexError(): no arguments
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    IndexError

    >>> raise IndexError('spam')                    # Constructor argument attached, printed
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    IndexError: spam
'''
I = IndexError('spam')                                  # Available in object attribute
print(I)                                                # Displays args when printed manually
print(I.args)                                           # Attached constructor arguments


""" 
The same holds true for user-defined exceptions in Python 3.X, 
because they inherit the constructor and display methods present 
in their builtin superclasses:
""" 
class E(Exception): pass 
# raise E 
# raise E('spam')

I = E('spam')                                           # Available in object attribute
print(I)                                                # Displays args when printed manually
print(I.args)                                           # Attached constructor arguments


'''
When intercepted in a try statement, the exception instance object gives access to both
the original constructor arguments and the display method:
'''
try:
    raise E('spam')
except E as err:
    print()
    print(err)
    print(err.args)
    print(repr(err))
    print(err.__class__)


# Multiple arguments save/display a tuple
try:
    raise E('spam', 'eggs', 'toast')
except E as err:
    print()
    print('%s %s' % (err, err.args))


""" 
Note that exception instance objects are not strings themselves, but use the __str__
operator overloading protocol
"""


"Custom Print Displays"
'''
instances of class-based exceptions display whatever you passed 
to the class constructor when they are caught and printed:
'''
class MyBad(Exception): pass 

try: 
    raise MyBad("Sorry--my mistake!")
except MyBad as X:
    print()
    print('Caught', X)


""" 
To provide a more custom display, though, you can
define one of two string-representation overloading methods in your class (__repr__ or
__str__) to return the string you want to display for your exception.
""" 
class MyBad(Exception):
    def __str__(self):
        return "Always look on the bright side of life..."
    

try: 
    raise MyBad() 
except MyBad as X:
    print(X) 



"Custom Data and Behavior"
'''
Besides supporting flexible hierarchies, exception classes also provide storage for extra
state information as instance attributes.
'''
class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
    
def parser():
    raise FormatError(42, 'spam.txt')               # When error found 

try:
    parser() 
except FormatError as X:
    print()
    print('Error at', X.file, X.line)


class FormatError(Exception): pass                  # Inherited constructor 

def parser():
    raise FormatError(42, 'spam.txt')               # No Keywords allowed 

try:
    parser() 
except FormatError as X:
    print()
    print('Error at', X.args[0], X.args[1])         # Not specific to this app 

