"String Representation: __repr__ and __str__"
class adder:
    def __init__(self, value=0):
        self.data = value                           # Initialize data
    
    def __add__(self, other):
        self.data += other                          # Add other in place (bad form?)

if __name__ == '__main__':
    x = adder()                     # Default displays
    print(x)


"""
But coding or inheriting string representation methods allows us to customize the display—
as in the following, which defines a __repr__ method in a subclass that returns
a string representation for its instances.
"""
class addrepr(adder):                                   # # Inherit __init__, __add__
    def __repr__(self): #                               # Add string representation
        return 'addrepr(%s)' % self.data                # Convert to as-code string


if __name__ == '__main__':
    x = addrepr(2)                      # Runs __init__
    x + 1                               # Runs __add__ (x.add() better?)
    print(x)

    x                                   # Runs __repr__(on CMD)
    print(str(x), repr(x))              # Runs __repr__ for both


"""
If defined, __repr__ (or its close relative, __str__) is called automatically when class
instances are printed or converted to strings.

In particular, Python provides two display methods to support alternative
displays for different audiences:
    • __str__ is tried first for the print operation and the str built-in function (the internal
    equivalent of which print runs). It generally should return a user-friendly
    display.

    • __repr__ is used in all other contexts: for interactive echoes, the repr function, and
    nested appearances, as well as by print and str if no __str__ is present. It should
    generally return an as-code string that could be used to re-create the object, or a
    detailed display for developers.

__str__ is generally preferred for larger
user-friendly displays, and __repr__ for lower-level or as-code displays and all-inclusive
roles.
"""
class addstr(adder):
    def __str__(self):                                  # __str__ but no __repr__
        return '[Value: %s]' % self.data                # Convert to nice string


if __name__ == '__main__':
    x = addstr(3)
    x + 1

    repr(x)                                   # Default __repr__(on CMD)
    print(x)

    print(str(x), repr(x))
   

"""
__repr__ may be best if you want a single display for all contexts. By
defining both methods, though, you can support different displays in different contexts
"""
class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data                        # User-friendly string
    def __repr__(self):
        return 'addboth(%s)' % self.data                        # As-code string


if __name__ == '__main__':
    print()
    x = addboth(4)
    x + 1

    print(repr(x))                      # Runs __repr__
    print(x)                            # Runs __str__

    print(str(x), repr(x))

