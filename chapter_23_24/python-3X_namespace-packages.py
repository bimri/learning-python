"3.3 Python has four import models"
# From original to newest:
'''
- Basic module imports: import mod, from mod import attr
    The original model: imports of files and their contents, relative to the sys.path
    module search path

- Package imports: import dir1.dir2.mod, from dir1.mod import attr
    Imports that give directory path extensions relative to the sys.path module search
    path, where each package is contained in a single directory and has an initialization
    file, in Python 2.X and 3.X

- Package-relative imports: from . import mod (relative), import mod (absolute)
    The model used for intrapackage imports of the prior section, with its relative or
    absolute lookup schemes for dotted and nondotted imports, available but differing
    in Python 2.X and 3.X

- Namespace packages: import splitdir.mod
    The new namespace package model, which allows packages
    to span multiple directories, and requires no initialization file, introduced in Python 3.3
'''


"Namespace Package Semantics"
'''
new-style namespace packages cannot contain an
__init__.py, and may span multiple directories that are collected at import time

none of the directories that make up a namespace package can have an __init__.py, but
the content nested within each of them is treated as a single package


while looking for an imported module or package named spam, for each directory in
the module search path, Python tests for a wider variety of matching criteria, in the
following order:
    1. If directory\spam\__init__.py is found, a regular package is imported and returned.
    2. If directory\spam.{py, pyc, or other module extension} is found, a simple module
       is imported and returned.
    3. If directory\spam is found and is a directory, it is recorded and the scan continues
       with the next directory in the search path.
    4. If none of the above was found, the scan continues with the next directory in the
       search path.

If the search path scan completes without returning a module or package by steps 1 or
2, and at least one directory was recorded by step 3, then a namespace package is created.       

The creation of the namespace package happens immediately, and is not deferred until
a sublevel import occurs. The new namespace package has a __path__ attribute set to
an iterable of the directory path strings that were found and recorded during the scan
by step 3, but does not have a __file__.

The __path__ attribute is then used in later, deeper accesses to search all package components—
each recorded entry on a namespace package’s __path__ is searched whenever
further nested items are requested, much like the sole directory of a regular package.

Viewed another way, the __path__ attribute of a namespace package serves the same
role for lower-level components that sys.path does at the top for the leftmost component
of package import paths; it becomes the “parent path” for accessing lower items
using the same four-step procedure just sketched.

The net result is that a namespace package is a sort of virtual concatenation of directories
located via multiple sys.path entries. Once a namespace package is created, though,
there is no functional difference between it and a regular package; it supports everything
we’ve learned for regular packages, including package-relative import syntax.
'''