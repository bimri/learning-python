"Imports Versus Scopes"
'''
A variable’s meaning is always determined by the locations of assignments in your source
code, and attributes are always requested of an object explicitly.
'''
X = 88                              # My X: global to this file only
def f():
    global X                        # Change this file's X
    X = 99                          # Cannot see names in other modules
