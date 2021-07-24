"User-Defined Exceptions"
'''
User-defined exceptions are coded with classes, which inherit from a built-in exception class: 
usually the class named Exception:
'''
class AlreadyGotOne(Exception):                             # User-defined exception class
    pass

def grail():
    raise AlreadyGotOne()                                   # Raise an instance


try:
    grail()
except AlreadyGotOne:
    print('You already got the grail!')


""" 
Class-based exceptions allow scripts to build exception categories,
which can inherit behavior, and have attached state information and methods. They
can also customize their error message text displayed if they’re not caught:
""" 
class Career(Exception):
    def __str__(self): return 'So I became a waiter...'


raise Career()                                              # Raise an instance
