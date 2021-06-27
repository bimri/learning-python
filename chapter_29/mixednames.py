class MixedNames:                                           # Define class
    data = 'spam'                                           # Assign class attr
    def __init__(self, value):                              # Assign method name
        self.data = value                                    # Assign instance
    def display(self):
        print(self.data, MixedNames.data)                   # Instance attr, class attr


'''
Like all class attributes, this data is inherited and shared by all instances of the
class that don’t have data attributes of their own.

When we make instances of this class, the name data is attached to those instances by
the assignment to self.data in the constructor method:

The net result is that data lives in two places: in the instance objects (created by the
self.data assignment in __init__), and in the class from which they inherit names
(created by the data assignment in the class).
'''
x = MixedNames(1)                           # Make two instance objects
y = MixedNames(2)                           # Each has its own data

print(x.display())                          # self.data differs, MixedNames.data is the same
print(y.display())


'''
When attached to classes, names are shared; in instances, names
record per-instance data, not shared behavior or data.
'''