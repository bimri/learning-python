'''
sys.path is initialized on startup, but thereafter you can
delete, append, and reset its components however you like:

    >>> import sys
    >>> sys.path
    ['', 'c:\\temp', 'C:\\Windows\\system32\\python33.zip', ...more deleted...]

    >>> sys.path.append('C:\\sourcedir')                                            # Extend module search path
    >>> import string                                                               # All imports search the new dir last

Once you’ve made such a change, it will impact all future imports anywhere while a
Python program runs, as all importers share the same single sys.path list (there’s only
one copy of a given module in memory during a program’s run—that’s why reload
exists). In fact, this list may be changed arbitrarily:

    >>> sys.path = [r'd:\temp']                                                     # Change module search path
    >>> sys.path.append('c:\\lp5e\\examples')                                       # For this run (process) only
    >>> sys.path.insert(0, '..')
    >>> sys.path
    ['..', 'd:\\temp', 'c:\\lp5e\\examples']
    >>> import string
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ImportError: No module named 'string'
'''

"""
Thus, you can use this technique to dynamically configure a search path inside a Python
program. Be careful, though: if you delete a critical directory from the path, you may
lose access to critical utilities.

Also, remember that such sys.path settings endure for only as long as the Python session
or program (technically, process) that made them runs; they are not retained after
Python exits. By contrast, PYTHONPATH and .pth file path configurations live in the operating
system instead of a running Python program, and so are more global: they are
picked up by every program on your machine and live on after a program completes.
On some systems, the former can be per-user and the latter can be installation-wide.
"""
