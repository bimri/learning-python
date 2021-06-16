# Global scope
X = 99                                  # X and func assigned in module: global

def func(Y):                            # Y and Z assigned in function: locals
    # Local scope
    Z = X + Y                           # X is global
    return Z

print(
    func(1)                             # func in module: result=100
)


'''
names in the local scope may override variables of the same name in 
both the global and built-in scopes, and global names may override 
built-ins
'''
def hider():
    open = 'spam'                               # Local variable, hides built-in here
    ...
    open('data.txt')                            # Error: this no longer opens a file in this scope!


'redefining a built-in name is often a bug'
'a nasty one at that, because Python will not'
'issue a warning message about it.'
"don’t redefine a built-in name you need"


'''
Note that functions can similarly hide global 
variables of the same name with locals
'''
K = 88                                  # Global K

def func():
    K = 99                              # Local K: hides global, but we want this here

func()
print(K)                                # Prints 88: unchaged

'''
there is no way to change a name outside a function without adding a
global (or nonlocal) declaration to the def
'''
