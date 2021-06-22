# modules and nested directory structure
# with two subdirectories named sub located in different parent
# directories, dir1 and dir2:
'''
C:\code\ps\dir1\sub\mod1.py
C:\code\ps\dir2\sub\mod2.py


c:\code> mkdir ns\dir1\sub                                  # Two dirs of same name in different dirs
c:\code> mkdir ns\dir2\sub                                  # And similar outside Windows

c:\code> type ns\dir1\sub\mod1.py                           # Module files in different directories
print(r'dir1\sub\mod1')

c:\code> type ns\dir2\sub\mod2.py
print(r'dir2\sub\mod2')

c:\code> set PYTHONPATH=C:\code\ps\dir1;C:\code\ps\dir2



c:\code> C:\Python33\python
>>> import sub
>>> sub # Namespace packages: nested search paths
<module 'sub' (namespace)>
>>> sub.__path__
_NamespacePath(['C:\\code\\ns\\dir1\\sub', 'C:\\code\\ns\\dir2\\sub'])

>>> from sub import mod1
dir1\sub\mod1
>>> import sub.mod2 # Content from two different directories
dir2\sub\mod2

>>> mod1
<module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>

>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>



c:\code> C:\Python33\python
>>> import sub.mod1
dir1\sub\mod1
>>> import sub.mod2 # One package spanning two directories
dir2\sub\mod2

>>> sub.mod1
<module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>

>>> sub
<module 'sub' (namespace)>
>>> sub.__path__
_NamespacePath(['C:\\code\\ns\\dir1\\sub', 'C:\\code\\ns\\dir2\\sub'])



c:\code> type ns\dir1\sub\mod1.py
from . import mod2 # And "from . import string" still fails
print(r'dir1\sub\mod1')

c:\code> C:\Python33\python
>>> import sub.mod1 # Relative import of mod2 in another dir
dir2\sub\mod2
dir1\sub\mod1
>>> import sub.mod2 # Already imported module not rerun
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
'''



"Namespace Package Nesting"
'''
c:\code> mkdir ns\dir2\sub\lower                            # Further nested components
c:\code> type ns\dir2\sub\lower\mod3.py
print(r'dir2\sub\lower\mod3')

c:\code> C:\Python33\python
>>> import sub.lower.mod3                                   # Namespace pkg nested in namespace pkg
dir2\sub\lower\mod3
c:\code> C:\Python33\python
>>> import sub                                              # Same effect if accessed incrementally
>>> import sub.mod2
dir2\sub\mod2
>>> import sub.lower.mod3
dir2\sub\lower\mod3

>>> sub.lower                                               # A single-directory namespace pkg
<module 'sub.lower' (namespace)>
>>> sub.lower.__path__
_NamespacePath(['C:\\code\\ns\\dir2\\sub\\lower'])



c:\code> mkdir ns\dir1\sub\pkg
C:\code> type ns\dir1\sub\pkg\__init__.py
print(r'dir1\sub\pkg\__init__.py')

c:\code> C:\Python33\python
>>> import sub.mod2                                         # Nested module
dir2\sub\mod2
>>> import sub.pkg                                          # Nested regular package
dir1\sub\pkg\__init__.py
>>> import sub.lower.mod3                                   # Nested namespace package
dir2\sub\lower\mod3

>>> sub # Modules, packages,and namespaces
<module 'sub' (namespace)>
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
>>> sub.pkg
<module 'sub.pkg' from 'C:\\code\\ns\\dir1\\sub\\pkg\\__init__.py'>
>>> sub.lower
<module 'sub.lower' (namespace)>
>>> sub.lower.mod3
<module 'sub.lower.mod3' from 'C:\\code\\ns\\dir2\\sub\\lower\\mod3.py'>
'''



"Files Still Have Precedence over Directories"
'''
c:\code> mkdir ns2
c:\code> mkdir ns3
c:\code> mkdir ns3\dir
c:\code> notepad ns3\dir\ns2.py
c:\code> type ns3\dir\ns2.py
print(r'ns3\dir\ns2.py!')


c:\code> set PYTHONPATH=
c:\code> py −3.2
>>> import ns2
ImportError: No module named ns2
c:\code> py −3.3
>>> import ns2
>>> ns2                                                     # A single-directory namespace package in CWD
<module 'ns2' (namespace)>
>>> ns2.__path__
_NamespacePath(['.\\ns2'])



c:\code> set PYTHONPATH=C:\code\ns3\dir
c:\code> py −3.3
>>> import ns2                                              # Use later module file, not same-named directory!
ns3\dir\ns2.py!
>>> ns2
<module 'ns2' from 'C:\\code\\ns3\\dir\\ns2.py'>

>>> import sys
>>> sys.path[:2]                                            # First '' means current working directory, CWD
['', 'C:\\code\\ns3\\dir']

c:\code> py −3.2
>>> import ns2
ns3\dir\ns2.py!
>>> ns2
<module 'ns2' from 'C:\code\ns3\dir\ns2.py'>


c:\code> mkdir ns4\dir1\sub
c:\code> mkdir ns4\dir2\sub
c:\code> set PYTHONPATH=c:\code\ns4\dir1;c:\code\ns4\dir2
c:\code> py −3
>>> import sub
>>> sub
<module 'sub' (namespace)>
>>> sub.__path__
_NamespacePath(['c:\\code\\ns4\\dir1\\sub', 'c:\\code\\ns4\\dir2\\sub'])


c:\code> notepad ns4\dir2\sub\__init__.py
c:\code> py −3
>>> import sub # Use later reg. package, not same-named directory!
>>> sub
<module 'sub' from 'c:\\code\\ns4\\dir2\\sub\\__init__.py'>
'''
