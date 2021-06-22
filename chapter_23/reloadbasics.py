'''
Unlike import and from:
    • reload is a function in Python, not a statement.
    • reload is passed an existing module object, not a new name.
    • reload lives in a module in Python 3.X and must be imported itself.
'''

'''
import module                               # Initial import
...use module.attributes...
...                                         # Now, go change the module file
...
from imp import reload                      # Get reload itself (in 3.X)
reload(module)                              # Get updated exports
...use module.attributes...

Perhaps the most important thing to know about reload is that it
changes a module object in place; it does not delete and re-create the module object.

Because of that, every reference to an entire module object anywhere in your program
is automatically affected by a reload.
'''
