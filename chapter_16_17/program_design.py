'''
Functions should rely on arguments and 
return values instead of globals.

variables assigned in a def are local by default 
because that is normally the best policy
'''


"Changing globals can lead to well-known software engineering problems"
# They are dependent on—that is,
# coupled with—the global variable
X = 34
def func1():
    global X
    X = 8

def func2():
    global X
    X = 77

# value of X is timing-dependent
# as it depends on which function was called last


'''
Local variables disappear when the function
returns, but globals do not!
'''

"General rule of thumb"
# Try to communicate with passed-in 
# arguments and return values instead



"Program Design: Minimize Cross-File Changes"
'''
# first.py
X = 99                                                          # This code doesn't know about second.py

# second.py
import first
print(first.X)                                                  # OK: references a name in another file
first.X = 88                                                    # But changing it can be too subtle and implicit


the best way to communicate across 
file boundaries is to call functions, 
passing in arguments and getting back
return values


we would probably be better off coding an accessor
function to manage the change
# first.py
X = 99

def setX(new):                                                  # Accessor make external changes explit
    global X                                                    # And can manage access in a single place
    X = new

# second.py
import first
first.setX(88)                                                  # Call the function instead of changing directly
'''
