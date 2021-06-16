'''
-> break
    Jumps out of the closest enclosing loop (past the entire loop statement)
-> continue
    Jumps to the top of the closest enclosing loop (to the loop’s header line)
-> pass
    Does nothing at all: it’s an empty statement placeholder
-> Loop else block
    Runs if and only if the loop is exited normally (i.e., without hitting a break)
'''

# General Loop Format
'''
while test:
    statements
    if test: break                          # Exit loop now, skip else if present
    if test: continue                       # Go to top of loop now, to test
else:
    statements                              # Run if we didn't hit a 'break'
'''


# PASS
# while True: pass                            # Type Ctrl-C to stop me!

def func1():
    pass                                    # Add real code here later

def func2():
    pass


# ...(alternative for pass)
def func1():
    ...

def func1():
    ...

func1()                                         # Does nothing if called

# Works on same line too
def func1(): ...
def func2(): ...


# Alternative to None
X = ...
print(X)
