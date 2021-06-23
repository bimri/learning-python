"Module Design Concepts"
'''
• You’re always in a module in Python.
     - There’s no way to write code that doesn’t live in some module.
     - even code typed at the interactive prompt really goes in a built-in module called __main__;
     - the only unique things about the interactive prompt are that code runs and is discarded 
       immediately, and expression results are printed automatically.

• Minimize module coupling: global variables.
    - Like functions, modules work best if they’re written to be closed boxes.
    - As a rule of thumb, they should be as independent of global variables 
      used within other modules as possible, except forfunctions and classes imported from them.
    - The only things a module should share with the outside world are the tools it uses, and 
      the tools it defines.

• Maximize module cohesion: unified purpose. 
    - You can minimize a module’s couplings by maximizing its cohesion; if all the components of a module share a
      general purpose, you’re less likely to depend on external names.  

• Modules should rarely change other modules’ variables. 
    - it’s perfectly OK to use globals defined in another module (that’s how clients import services, after all),
      but changing globals in another module is often a symptom of a design problem.
    - There are exceptions, of course, but you should try to communicate results through
      devices such as function arguments and return values, not cross-module changes.
    -  Otherwise, your globals’ values become dependent on the order of arbitrarily remote
      assignments in other files, and your modules become harder to understand
      and reuse.
'''

"Data Hiding in Modules"
'a Python module exports all the names assigned at the top level of its file.'
'There is no notion of declaring which names should and shouldn’t be visible outside the module.'
'there’s no way to prevent a client from changing names inside a module if it wants to.'
# In Python, data hiding in modules is a convention, not a syntactical constraint.


"Minimizing from * Damage: _X and __all__"
'''
you can prefix names with a single underscore (e.g., _X) to prevent
them from being copied out when a client imports a module’s names with a from *
statement.

This really is intended only to minimize namespace pollution; because from
* copies out all names, the importer may get more than it’s bargained for (including
names that overwrite names in the importer).

Underscores aren’t “private” declarations:
you can still see and change such names with other import forms, such as the
import statement:
'''



"""
you can achieve a hiding effect similar to the _X naming convention by
assigning a list of variable name strings to the variable __all__ at the top level of the
module.

When this feature is used, the from * statement will copy out only those names
listed in the __all__ list.

In effect, this is the converse of the _X convention: __all__
identifies names to be copied, while _X identifies names not to be copied. Python looks
for an __all__ list in the module first and copies its names irrespective of any underscores;
if __all__ is not defined, from * copies all names without a single leading underscore:
"""