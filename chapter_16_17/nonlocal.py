"nonlocal in Action"
def tester(start):
    state = start
    def nested(label):
        print(label, state)                             # Remembers state in enclosing scope
    return nested

F = tester(0)
F('Spam')
F('Ham')

"Using nonlocal for changes"
def tester(start):
    state = start
    def nested(label):
        nonlocal state                                  # Rems state in enclosing scope
        print(label, state)
        state += 1                                      # Allowed to change it if nonlocal
    return nested

F = tester(0)
F('Pauline')                                            # Increments state on each call
F('Cyso')
F('Chnch')

G = tester(40)                                          # Make a new tester that starts at 40
G('Rap')
G('HipHop')
G('Rock')                                               # My state information updated to 42


"Boundary cases"                # SyntaxError: no binding for nonlocal 'state' found
# def tester(start):
#     def nested(label):
#         nonlocal state                                  # Nonlocals must already exist in enclosing def!
#         state = 0
#         print(label, state)
#     return nested


"Globals don't have to exist yet when declared"
def tester(start):
    def nested(label):
        global state                                    # Globals don't have to exist yet when declared
        state = 0                                       # This creates the name in the module now
        print(label, state)
    return nested

F = tester(0)
F('abs')
print(state)


"nonlocal restricts the scope lookup to just enclosing defs"   # SyntaxError: no binding for nonlocal 'spam' found
# spam = 99 
# def tester():
#     def nested():
#         nonlocal spam                                   # MUST BE IN THE DEF NOT THE MODULE
#         print('Current',  spam)
#         spam += 1
#     return nested
