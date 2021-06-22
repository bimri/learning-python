'''
from .string import name1, name2                            # Imports names from mypkg.string
from . import string                                        # Imports mypkg.string
from .. import string                                       # Imports string sibling of mypkg


Besides making intrapackage imports more explicit, this feature is designed in part to
allow scripts to resolve ambiguities that can arise when a same-named file appears in
multiple places on the module search path. Consider the following package directory:
        mypkg\
            __init__.py
            main.py
            string.py

Now, suppose that the main module tries to import a module named
string. In Python 2.X and earlier, Python will first look in the mypkg directory to perform
a relative import.

It will find and import the string.py file located there, assigning
it to the name string in the mypkg.main module’s namespace.
'''
# Imports string outside package (absolute)
import string

"A from import without leading-dot syntax is considered absolute"
# Imports name from string outside package
from string import name 



'''
If you really want to import a module from your package without giving its full path
from the package root, though, relative imports are still possible if you use the dot
syntax in the from statement:
'''
# Imports mypkg.string here (relative)
from . import string 


"We can also copy specific names from a module with relative syntax:"
# Imports names from mypkg.string
from .packagefiles import name1, name2


"An additional leading dot performs the relative import starting from the parent of the current package."
# Imports a sibling of mypkg
# from ..import spam


'code located in some module A.B.C can use any of these forms:'
"""
from . import D                                             # Imports A.B.D (. means A.B)
from .. import E                                            # Imports A.E (.. means A)
from .D import X                                            # Imports A.B.D.X (. means A.B)
from ..E import X                                           # Imports A.E.X (.. means A)
"""


"Relative imports versus absolute package paths"
'''
a file can sometimes name its own package explicitly in an absolute import
statement, relative to a directory on sys.path.

this relies on both the configuration and the order of the module search path
settings, while relative import dot syntax does not.

this form requires that the
directory immediately containing mypkg be included in the module search path.
'''
# from mypkg import string                                  # Imports mypkg.string (absolute)


'''
If mypkg isn’t the package’s root, absolute import statements must list all the directories
below the package’s root entry in sys.path when naming packages explicitly like this:
'''
# from system.section.mypkg import string                   # system container on sys.path only


"In large or deep packages, that could be substantially more work to code than a dot:"
# from . import string                                      # Relative import syntax
