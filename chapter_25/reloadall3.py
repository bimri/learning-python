'''
there is usually an explicit stack or queue equivalent to most
recursive functions, which may be preferable in some contexts. The following is one
such transitive reloader; it uses a generator expression to filter out nonmodules and
modules already visited in the current module’s namespace. Because it both pops and
adds items at the end of its list, it is stack based, though the order of both pushes and
dictionary values influences the order in which it reaches and reloads modules—it visits
submodules in namespace dictionaries from right to left, unlike the left-to-right order
of the recursive versions (trace through the code to see how). We could change this,
but dictionary order is arbitrary anyhow.
'''

"""
reloadall3.py: transitively reload nested modules (explicit stack)
"""
import types
from importlib import reload # from required in 3.X
from reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop() # Delete next item at end
        status(next) # Reload this, push attrs
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')                                    # Test code: reload myself?
