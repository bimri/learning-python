"Classes Are Attributes in Modules"
'''
    from modulename import FirstClass                           # Copy name into my scope
    class SecondClass(FirstClass):                              # Use class name directly
        def display(self): ...

Or, equivalently:
    import modulename                                           # Access the whole module
    class SecondClass(modulename.FirstClass):                   # Qualify to reference
        def display(self): ...
'''


# food.py
var = 1 # food.var
def func(): ...                             # food.func
class spam: ...                             # food.spam
class ham: ...                              # food.ham
class eggs: ...                             # food.eggs


# person.py
class person: ...

"we need to go through the module to fetch the class as usual:"
import person                               # Import module
x = person.person()                         # Class within module

"Saying just person gets the module, not the class, unless the from statement is used:"
from person import person                   # Get class from module
x = person()                                # Use class name


"common convention in Python dictates that class names should begin with an uppercase letter, to help make them more distinct:"
import person                               # Lowercase for modules
x = person.Person()                         # Uppercase for classes
