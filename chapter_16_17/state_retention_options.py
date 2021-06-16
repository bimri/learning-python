"State with nonlocal"
def tester(start):
    state = start                                       # Each call gets its own state
    def nested(label):
        nonlocal state                                  # Remembers state in enclosing scope
        print(label, state)
        state += 1                                      # Allowed to change it if nonlocal
    return nested

F = tester(0)
F('Python')                                             # State visible within closure only

# F.state                                                 # AttributeError: 'function' object has no attribute 'state'


"State with Globals: A Single Copy Only"
def tester(start):
    global state                                        # Move it out to the module to change it
    state = start
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('Wolfram')
F('Dart')

# 👆🏾 only allows for a single shared copy of the
# state information in the module scope
G = tester(43)                                          # Resets state's single copy in global scope
G('toast')
G('bacon')

# prior calls will see their state overwritten
F('JavaScript')                                         # But my counter has been overwritten!



"State with Classes: Explicit Attributes (Preview)"
class tester:                                           # Class-based alternative
    def __init__(self, start):                          # On object construction
        self.state = start                              # save state explicitly in new object
    def nested(self, label):
        print(label, self.state)                        # Reference state explicitly
        self.state += 1                                 # Changes are always allowed
    

F = tester(0)                                           # Create instance, invoke __init__
F.nested('AfroBeats')                                   # F is passed to self
F.nested('Reggae')

G = tester(43)                                          # Each instance gets new copy of state
G.nested('Jay Z')                                       # Changing one does not impact others
G.nested('Kanye West')

F.nested('Jazz')                                        # F's state is where it left off
print(F.state )                                                # State may be accessed outside class


'''
class objects look like callable 
functions using operator overloading
'''
class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):                          # Intercept direct instance calls
        print(label, self.state)                        # So .nested() not required
        self.state += 1

H = tester(99)
H('Juice')                                              # Invokes __call__
H('Pancakes')


"State with Function Attributes"
'''
state to be accessed externally, and saves a line 
by not requiring a nonlocal declaration
'''
def tester(start):
    def nested(label):
        print(label, nested.state)                      # nested is in enclosing scope
        nested.state += 1                               # Change attr, not nested itself
    nested.state = start                                # Initial state after func defined
    return nested

F = tester(0)
F('spam')                                               # F is a 'nested' with state attached
F('ham')
print(
    F.state                                             # Can access state outside functions too
)


''''
Because each call to the outer function produces a new nested function object, this
scheme supports multiple copy per-call changeable data just like nonlocal closures and
classes—a usage mode that global variables cannot provide:
'''
G = tester(42)                                          # G has own state, doesn't overwrite F's
G('eggs')

F('ham')

print(F.state)                                          # State is accessible and per-call
print(G.state)
print(F is G)                                           # Different function objects



"State with mutables: Obscure ghost of Pythons past?"
# possible to change a mutable object in the enclosing scope
# in 2.X and 3.X without declaring its name nonlocal
def tester(start):
    def nested(label):
        print(label, state[0])                          # Leverage in-place mutable change
        state[0] += 1                                   # Extra syntax, deep magic?
    state = [start]
    return nested
print()


"Customizing open"
import builtins

def makeopen(id):
    original = builtins.open
    def custom(*kargs, **pargs):
        print('Custom open call %r:' % id, kargs, pargs)
        return original(*kargs, **pargs)
    builtins.open = custom

F = open(r'E:\practice\learning_python\chapter_16\script2.py')                                      # Call built-in open in builtins
print(F.read())

makeopen('spam file')                                                                               # Custom open calls built-in open

F = open(r'E:\practice\learning_python\chapter_16\script2.py')                                      # Call custom open in builtins
print(F.read())


makeopen('eggs')                                                                                    # Nested customizers work too!
F = open(r'E:\practice\learning_python\chapter_16\script2.py')                                      # Because each retains own state
print(F.read())


"Class Based Version"
import builtins


class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self
    def __call__(self, *kargs, **pargs):
        print('Custom open call %r:' % self.id, kargs, pargs)
        return self.original(*kargs, **pargs)
