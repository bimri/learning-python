"Computed Attributes"

class AttrSquare:
    def __init__(self, start):
        self.value = start 
    
    def __getattr__(self, attr):                        # undefined attr fetch
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)
        
    def __setattr__(self, attr, value):                 # On all attr assignments
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value


# this script’s mechanics are based on generic attribute interception methods:
A = AttrSquare(3)           # 2 instance of class with overloading
B = AttrSquare(32)          # Each has different state information

print(A.X)                  # 3 ** 2
A.X = 4
print(A.X)                  # 4 ** 2
print(B.X)                  # 32 ** 2 (1024)


'Using __getattribute__'
class AttrSquare:
    def __init__(self, start):
        self.value = start                              # Triggers __setattr__! 
    
    def __getattribute__(self, attr):                   # undefined attr fetch
        if attr == 'X':
            return self.value ** 2                      # Triggers __getattribute__ again!
        else:
            raise AttributeError(attr)
        
    def __setattr__(self, attr, value):                 # On all attr assignments
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value
    
print('*'*10)
print(A.X)                  # 3 ** 2
A.X = 94
print(A.X)                  # 94 ** 2
print(B.X)                  # 32 ** 2 (1024)


"""
When this version, getattribute-computed.py, is run, the results are the same again.
Notice, though, the implicit routing going on inside this class’s methods:

    • self.value=start inside the constructor triggers __setattr__
    • self.value inside __getattribute__ triggers __getattribute__ again

In fact, __getattribute__ is run twice each time we fetch attribute X. This doesn’t happen
in the __getattr__ version, because the value attribute is not undefined. If you care
about speed and want to avoid this, change __getattribute__ to use the superclass to
fetch value as well:
"""
def __getattribute__(self, attr):
    if attr == 'X':
        return object.__getattribute__(self, 'value') ** 2
