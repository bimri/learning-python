"Display Usage Notes"
'''
Though generally simple to use, I should mention three usage notes regarding these
methods here. First, keep in mind that __str__ and __repr__ must both return strings;
other result types are not converted and raise errors, so be sure to run them through a
to-string converter (e.g., str or %) if needed.

Second, depending on a container’s string-conversion logic, the user-friendly display
of __str__ might only apply when objects appear at the top level of a print operation;
objects nested in larger objects might still print with their __repr__ or its default.

Third, and perhaps most subtle, the display methods also have the potential to trigger
infinite recursion loops in rare contexts—because some objects’ displays include displays
of other objects, it’s not impossible that a display may trigger a display of an object
being displayed, and thus loop.

In practice, __str__, and its more inclusive relative __repr__, seem to be the second
most commonly used operator overloading methods in Python scripts, behind
__init__.
'''
class Printer:
    def __init__(self, val):
        self.val = val
    def __str__(self):                                  # Used for instance itself
        return str(self.val)                            # Convert to a string result
    

if __name__ == '__main__':
    objs = [Printer(2), Printer(3)]
    for x in objs: print(x)                 # __str__ run when instance printed
                                            # But not when instance is in a list!
    print(objs)
    str(objs)


'''
To ensure that a custom display is run in all contexts regardless of the container, code
__repr__, not __str__; the former is run in all cases if the latter doesn’t apply, including
nested appearances:
'''    
class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):                                 # __repr__ used by print if no __str__                    # Used for instance itself
        return str(self.val)                            # __repr__ used if echoed or nested
    

if __name__ == '__main__':
    print()
    objs = [Printer(2), Printer(3)]
    for x in objs: print(x)                 # No __str__: runs __repr__

    print(objs)                             # Runs __repr__, not ___str__
    repr(x)
    