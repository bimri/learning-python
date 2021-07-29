"The assert Statement"
""" 
As a somewhat special case for debugging purposes, Python includes the assert statement.
It is mostly just syntactic shorthand for a common raise usage pattern, and an
assert can be thought of as a conditional raise statement. A statement of the form:
    assert test, data               # The data part is optional 

works like the following code:    
""" 
if __debug__:
        if not test:
            raise AssertionError(data)


'''
In other words, if the test evaluates to false, Python raises an exception: the data item
(if it’s provided) is used as the exception’s constructor argument. Like all exceptions,
the AssertionError exception will kill your program if it’s not caught with a try, in
which case the data item shows up as part of the standard error message.
'''

""" 
As an added feature, assert statements may be removed from a compiled program’s
byte code if the -O Python command-line flag is used, thereby optimizing the program.
AssertionError is a built-in exception, and the __debug__ flag is a built-in name that is
automatically set to True unless the -O flag is used. Use a command line like python –O
main.py to run in optimized mode and disable (and hence skip) asserts.
""" 
