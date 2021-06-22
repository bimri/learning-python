'''
The net effect is that this example’s directory structure should be as follows, with indentation
designating directory nesting:
dir0\                                           # Container on module search path
    dir1\
        __init__.py
        dir2\
            __init__.py
            mod.py

The __init__.py files can contain Python code, just like normal module files. Their
names are special because their code is run automatically the first time a Python program
imports a directory, and thus serves primarily as a hook for performing initialization
steps required by the package.

These files can also be completely empty, though,
and sometimes have additional roles
'''


'''
file named __init__.py has been lifted as of Python 3.3. In that
release and later, directories of modules with no such file may be imported
as single-directory namespace packages, which work the same
but run no initialization-time code file.
'''
