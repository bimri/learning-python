X = 99                                      # Global scope name: not used

def f1():
    X = 88                                  # Enclosing def local
    def f2():
        print(X)                            # Reference made in nested def
    f2()

f1()                                        # Prints 88: enclosing def local


'''
This enclosing scope lookup works even if the 
enclosing function has already returned
'''
def f1():
    X = 88
    def f2():
        print(X)                            # Remembers X in enclosing def scope
    return f2                               # Return f2 but don't call it

action = f1()                               # Make, return function
action()                                    # Call it now: prints 88
