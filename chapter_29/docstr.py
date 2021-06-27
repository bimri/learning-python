"Documentation Strings Revisited"
'''
Docstrings are string literals that show up at the top of various structures and are
automatically saved by Python in the corresponding objects’ __doc__ attributes.

This works for module files, function defs, and classes and methods.
'''

"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class Spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)


'''
The main advantage of documentation strings is that they stick around at runtime.
Thus, if it’s been coded as a docstring, you can qualify an object with its __doc__ attribute
to fetch its documentation (printing the result interprets line breaks if it’s a
multiline string):

    >>> import docstr
    >>> docstr.__doc__
    'I am: docstr.__doc__'
  
    >>> docstr.func.__doc__
    'I am: docstr.func.__doc__'
    >>> docstr.spam.__doc__
    'I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__'
    >>> docstr.spam.method.__doc__
    'I am: spam.method.__doc__ or self.method.__doc__'

    >>> x = docstr.spam()
    >>> x.method()
    I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__
    I am: spam.method.__doc__ or self.method.__doc__
'''

"""
    >>> help(docstr)
    Help on module docstr:
    
    NAME
        docstr - I am: docstr.__doc__
    
    FILE
        c:\code\docstr.py
    
    CLASSES
        spam
        
        class spam
            | I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__
            |
            | Methods defined here:
            |
            | method(self)
            | I am: spam.method.__doc__ or self.method.__doc__
    
    FUNCTIONS
        func(args)
            I am: docstr.func.__doc__
"""


'''
the Python “best practice” rule of thumb is to use docstrings for functional
documentation (what your objects do) and hash-mark comments for more micro-
level documentation
'''