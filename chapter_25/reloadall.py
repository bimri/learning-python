"A Recursive Reloader"
'''
A better approach is to write a general tool to do transitive reloads automatically by
scanning modules’ __dict__ namespace attributes and checking each item’s type to
find nested modules to reload. Such a utility function could call itself recursively to
navigate arbitrarily shaped and deep import dependency chains.
'''

"""
defines a reload_all function that automatically
reloads a module, every module that the module imports, and so on, all the way to the
bottom of each import chain. It uses a dictionary to keep track of already reloaded
modules, recursion to walk the import chains, and the standard library’s types module,
which simply predefines type results for built-in types. The visited dictionary technique
works to avoid cycles here when imports are recursive or redundant, because module
objects are immutable and so can be dictionary keys
"""

#!python
"""
reloadall.py: transitively reload nested modules (2.X + 3.X).
Call reload_all with one or more imported module module objects.
"""
import types 
from importlib import reload

def status(module):
    print('reloading ' + module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)
    
def transitive_reload(module, visited):
    if not module is visited:                                   # Trap cycles, duplicates
        status(module)                                          # Reload this module
        tryreload(module)                                       # And visit children
        visited[module] = True
        for attrobj in module.__dict__.values():                # For all attrs
            if type(attrobj) == types.ModuleType:               # Recur if modules
                transitive_reload(attrobj, visited)
            
def reload_all(*args):
    visited = {}                                                # Main entry point
    for arg in args:                                            # For all passed in
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):                                  # Self-test code
    import importlib, sys                                       # Import on tests only
    if len(sys.argv) > 1: modname = sys.argv[1]                 # command line(or passed)
    module = importlib.import_module(modname)                   # Import by name string
    reloader(module)                                            # Test passed-in reloader


if __name__ == '__main__':
    tester(reload_all, 'reloadall')                             # Test: reload myself?
