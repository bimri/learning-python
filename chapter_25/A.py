"Example: Transitive Module Reloads"
'''
When you reload a module, though, Python reloads only that particular
module’s file; it doesn’t automatically reload modules that the file being reloaded
happens to import.
'''

import chapter_25.alls                                # Not reloaded when A is!
import chapter_25.unders                              # Just an import of an already loaded module: no-ops

'''
% python
    >>> . . .
    >>> from imp import reload
    >>> reload(A)
'''

"""
By default, this means that you cannot depend on reloads to pick up changes in all the
modules in your program transitively—instead, you must use multiple reload calls to
update the subcomponents independently. This can require substantial work for large
systems you’re testing interactively. You can design your systems to reload their subcomponents
automatically by adding reload calls in parent modules like A, but this
complicates the modules’ code.
"""
