"Imports outside packages"
'''
C:\code> c:\Python33\python
>>> import string
>>> string
<module 'string' from 'C:\\Python33\\lib\\string.py'>
'''

# add a module of the same name in the directory we’re working in
# because the first entry on the module search path is the current working directory (CWD):
'''
# code\string.py
print('string' * 8)
C:\code> c:\Python33\python
>>> import string
stringstringstringstringstringstringstringstring
>>> string
<module 'string' from '.\\string.py'>
'''

"""
In other words, normal imports are still relative to the “home” directory (the top-level
script’s container, or the directory you’re working in). In fact, package relative import
syntax is not even allowed in code that is not in a file being used as part of a package:

>>> from . import string
SystemError: Parent module '' not loaded, cannot perform relative import


# code\main.py
import string                                               # Same code but in a file
print(string)

C:\code> C:\python33\python main.py                         # Equivalent results in 2.X
stringstringstringstringstringstringstringstring
<module 'string' from 'c:\\code\\string.py'>

Similarly, a from . import string in this nonpackage file fails the same as it does at the
interactive prompt—programs and packages are different file usage modes.
"""


"Imports within packages"
# get rid of the local string module we coded in the CWD and build a package
# directory there with two modules
"Package roots in this section are located in the CWD added automatically"
"to sys.path, so we don’t need to set PYTHONPATH"
'''
C:\code> del string* # del __pycache__\string* for bytecode in 3.2+
C:\code> mkdir pkg
c:\code> notepad pkg\__init__.py

# code\pkg\spam.py
import eggs                                                 # <== Works in 2.X but not 3.X!
print(eggs.X)

# code\pkg\eggs.py
X = 99999
import string
print(string)



# code\pkg\spam.py
from . import eggs # <== Use package relative import in 2.X or 3.X
print(eggs.X)

# code\pkg\eggs.py
X = 99999
import string
print(string)
C:\code> c:\Python27\python
>>> import pkg.spam
<module 'string' from 'C:\Python27\lib\string.pyc'>
99999
C:\code> c:\Python33\python
>>> import pkg.spam
<module 'string' from 'C:\\Python33\\lib\\string.py'>
99999
'''


"Import are still relative to the CWD"
'''
# code\string.py
print('string' * 8)

# code\pkg\spam.py
from . import eggs
print(eggs.X)

# code\pkg\eggs.py
X = 99999
import string                                               # <== Gets string in CWD, not Python lib!
print(string)
C:\code> c:\Python33\python                                 # Same result in 2.X
>>> import pkg.spam
stringstringstringstringstringstringstringstring
<module 'string' from '.\\string.py'>
99999
'''


"Selecting modules with relative and absolute imports"
'''
C:\code> del string*                                        # del __pycache__\string* for bytecode in 3.2+

# code\pkg\spam.py
import string                                               # <== Relative in 2.X, absolute in 3.X
print(string)

# code\pkg\string.py
print('Ni' * 8)


C:\code> c:\Python33\python
>>> import pkg.spam
<module 'string' from 'C:\\Python33\\lib\\string.py'>

C:\code> c:\Python27\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>



# code\pkg\spam.py
from . import string                                        # <== Relative in both 2.X and 3.X
print(string)

# code\pkg\string.py
print('Ni' * 8)

C:\code> c:\Python33\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from '.\\pkg\\string.py'>

C:\code> c:\Python27\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>
'''


"Relative imports search packages only"
'''
# code\pkg\spam.py
from . import string # <== Fails in both 2.X and 3.X if no string.py here!

C:\code> del pkg\string*

C:\code> C:\python33\python
>>> import pkg.spam
ImportError: cannot import name string

C:\code> C:\python27\python
>>> import pkg.spam
ImportError: cannot import name string
'''


"Imports are still relative to the CWD, again"
'''
# code\string.py
print('string' * 8)
# code\pkg\spam.py
 
from . import string                                        # <== Relative in both 2.X and 3.X
print(string)

# code\pkg\string.py
print('Ni' * 8)

C:\code> c:\Python33\python # Same result in 2.X
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from '.\\pkg\\string.py'>



# code\string.py
print('string' * 8)

# code\pkg\spam.py
import string # <== Relative in 2.X, "absolute" in 3.X: CWD!
print(string)

# code\pkg\string.py
print('Ni' * 8)

C:\code> c:\Python33\python
>>> import pkg.spam
stringstringstringstringstringstringstringstring
<module 'string' from '.\\string.py'>

C:\code> c:\Python27\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.pyc'>
'''
