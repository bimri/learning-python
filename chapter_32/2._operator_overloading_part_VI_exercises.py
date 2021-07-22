""" 
2. Operator overloading. Write a class called MyList that shadows (“wraps”) a Python
list: it should overload most list operators and operations, including +, indexing,
iteration, slicing, and list methods such as append and sort. See the Python reference
manual or other documentation for a list of all possible methods to support. Also,
provide a constructor for your class that takes an existing list (or a MyList instance)
and copies its components into an instance attribute. Experiment with your class
interactively. Things to explore:
    a. Why is copying the initial value important here?

    b. Can you use an empty slice (e.g., start[:]) to copy the initial value if it’s a
    MyList instance?

    c. Is there a general way to route list method calls to the wrapped list?

    d. Can you add a MyList and a regular list? How about a list and a MyList instance?

    e. What type of object should operations like + and slicing return? What about
    indexing operations?
    
    f. If you are working with a reasonably recent Python release (version 2.2 or
    later), you may implement this sort of wrapper class by embedding a real list
    in a standalone class, or by extending the built-in list type with a subclass.
    Which is easier, and why?
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


if __name__ == '__main__':
    x = MyList('bimri')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['inc'])
    print(x * 3)
    x.append('a')
    x.sort()
    print(' '.join(c for c in x))
    print(x.__len__())
    print(x.__getslice__(1, 3))
