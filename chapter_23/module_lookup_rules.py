'''

• Basic modules with simple names (e.g., A) are located by searching each directory
on the sys.path list, from left to right. 

• Packages are simply directories of Python modules with a special __init__.py file,
which enables A.B.C directory path syntax in imports. 
- In an import of A.B.C, for example, the directory named A is located relative to the normal module import
search of sys.path, B is another package subdirectory within A, and C is a module
or other importable item within B.

• Within a package’s files, normal import and from statements use the same
sys.path search rule as imports elsewhere. 
- Imports in packages using from statements and leading dots, however, are relative to the package; that is, only the
package directory is checked, and the normal sys.path lookup is not used. 
- In from .import A, for example, the module search is restricted to the directory containing
the file in which this statement appears.

'''