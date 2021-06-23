def tester():
    print("It's Christmas in Heaven...")

if __name__ == '__main__':                          # Only when run
    tester()                                        # Not when imported



'''
This module defines a function for clients to import and use as usual:

c:\code> python
>>> import runme
>>> runme.tester()
It's Christmas in Heaven...

But the module also includes code at the bottom that is set up to call the function
automatically when this file is run as a program:

c:\code> python runme.py
It's Christmas in Heaven...


In effect, a module’s __name__ variable serves as a usage mode flag, allowing its code to
be leveraged as both an importable library and a top-level script.

perhaps the most common way you’ll see the __name__ test applied is for
self-test code.
    you can package code that tests a module’s exports in the module
    itself by wrapping it in a __name__ test at the bottom of the file.

This way, you can use the file in clients by importing it, but also test its logic by running it from the system
shell or via another launching scheme.
'''


"""
Coding self-test code at the bottom of a file under the __name__ test is probably the most
common and simplest unit-testing protocol in Python. It’s much more convenient than
retyping all your tests at the interactive prompt.

In addition, the __name__ trick is also commonly used when you’re writing files that
can be used both as command-line utilities and as tool libraries.
"""
