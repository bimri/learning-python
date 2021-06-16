'''
The global statement and its nonlocal 3.X cousin are the only 
things that are remotely like declaration statements in Python
'''

"They are namespace declarations"
"Global tells Python that a function plans to change one or more global names"

# Global allows us to change names that live outised a def at the top level
# of a module file.

X = 56                          # Global X

def func():
    global X
    X = 90                      # Global X: outside def

func()
print(X)                        # Prints 90

"changing X inside the function changes the X outside it"


y, z = 1, 2                     # Global variables in module

def all_globals():
    global X                    # Declare globals assigned
    X = y + z                   # NO NEED to declare y,z: LNGB rule

all_globals()
print(X)

