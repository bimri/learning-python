""" 
3. Subclassing. Make a subclass of MyList from exercise 2 called MyListSub, which
extends MyList to print a message to stdout before each call to the + overloaded
operation and counts the number of such calls. MyListSub should inherit basic
method behavior from MyList. Adding a sequence to a MyListSub should print a
message, increment the counter for + calls, and perform the superclass’s method.
Also, introduce a new method that prints the operation counters to stdout, and
experiment with your class interactively. Do your counters count calls per instance,
or per class (for all instances of the class)? How would you program the other
option? (Hint: it depends on which object the count members are assigned to: class
members are shared by instances, but self members are per-instance data.)
""" 

class MyList:
    def __init__(self, start):
        #self.wrapped = start[:]                                        # Copy start: no side effects
        self.wrapped = list(start)                                      # Make sure it's a list here    
    def __add__(self, other):
        return MyList(self.wrapped + other)    
    def __mul__(self, time):
        return MyList(self.wrapped * time)    
    def __getitem__(self, offset):                                      # Also passed a slice in 3.X
        return self.wrapped[offset]                                     # For iteration if no __iter__    
    def __len__(self):
        return len(self.wrapped)    
    def __getslice__(self, low, high):                                  # Ignored in 3.X: uses __getitem__
        return MyList(self.wrapped[low:high])
    
    def append(self, node):
        self.wrapped.append(node)    
    def __getattr__(self, name):                                        # Other methods: sort/reverse/etc
        return getattr(self.wrapped, name)    
    def __repr__(self):                                                 # Catchall display method
        return repr(self.wrapped)
    

class MyListSub(MyList):
    calls = 0                                                           # Shared by instances
    def __init__(self, start):
        self.adds = 0                                                   # Varies in each instance
        MyList.__init__(self, start)
    
    def __add__(self, other):
        print('add: ' + str(other))
        MyListSub.calls += 1                                            # Class-wide counter
        self.adds += 1                                                  # Per-instance counts
        return MyList.__add__(self, other)
    
    def stats(self):
        return self.calls, self.adds                                    # All adds, my adds


if __name__ == '__main__':
    x = MyListSub('bimri')
    y = MyListSub('inc')
    print(x[2])
    print(x[1:])
    print(x + ['writes'])
    print(x + ['codes'])
    print(y + ['runs'])
    print(x.stats())
    print(y.stats())
