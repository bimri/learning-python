"""
Thanks
to their common testing function, we can run all three from a command line both with
no arguments to test the module reloading itself, and with the name of a module to be
reloaded listed on the command line (in sys.argv):
"""

'''
it’s hard to see here, we really are testing the individual reloader alternatives
—each of these tests shares a common tester function, but passes it the reload_all
from its own file.
    c:\code> reloadall.py
    reloading reloadall
    reloading types

    c:\code> reloadall2.py
    reloading reloadall2
    reloading types

    c:\code> reloadall3.py
    reloading reloadall3
    reloading types

Here are the variants reloading the 3.X tkinter GUI module and all
the modules its imports reach:
    c:\code> reloadall.py tkinter
    reloading tkinter
    reloading _tkinter
    reloading tkinter._fix
    ...etc...
    
    c:\code> reloadall2.py tkinter
    reloading tkinter
    reloading tkinter.constants
    reloading tkinter._fix
    ...etc...
    
    c:\code> reloadall3.py tkinter
    reloading tkinter
    reloading sys
    reloading tkinter.constants
    ...etc...


As usual we can test interactively, too, by importing and calling either a module’s main
reload entry point with a module object, or the testing function with a reloader function
and module name string:
    C:\code> py −3
    >>> import reloadall, reloadall2, reloadall3
    >>> import tkinter
    >>> reloadall.reload_all(tkinter)                                               # Normal use case
    reloading tkinter
    reloading tkinter._fix
    reloading os
    ...etc...
    
    >>> reloadall.tester(reloadall2.reload_all, 'tkinter')                          # Testing utility
    reloading tkinter
    reloading tkinter._fix
    reloading os
    ...etc...

    >>> reloadall.tester(reloadall3.reload_all, 'reloadall3')                       # Mimic self-test code
    reloading reloadall3
    reloading types


Finally, if you look at the output of tkinter reloads earlier, you may notice that each
of the three variants may produce results in a different order; they all depend on namespace
dictionary ordering, and the last also relies on the order in which items are added
to its stack.

To ensure that all three are reloading the same modules irrespective
of the order in which they do so, we can use sets (or sorts) to test for order-neutral
equality of their printed messages—obtained here by running shell commands with the
os.popen utility

    >>> import os
    >>> res1 = os.popen('reloadall.py tkinter').read()
    >>> res2 = os.popen('reloadall2.py tkinter').read()
    >>> res3 = os.popen('reloadall3.py tkinter').read()
    >>> res1[:75]
    'reloading tkinter\nreloading tkinter.constants\nreloading tkinter._fix\nreload'
    
    >>> res1 == res2, res2 == res3
    (False, False)
    >>> set(res1) == set(res2), set(res2) == set(res3)
    (True, True)
'''
