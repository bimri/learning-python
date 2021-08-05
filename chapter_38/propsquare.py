"Computed Attributes"
# properties do much more—computing the value of an attribute 
# dynamically when fetched

class PropSquare:
    def __init__(self, start):
        self.value = start     
    def getX(self):                                 # On attr fetch
        return self.value ** 2    
    def setX(self, value):                          # On attr assign
        self.value = value    
    X = property(getX, setX)                        # No delete or docs


P = PropSquare(3)               # Two instances of class with property
Q = PropSquare(32)              # Each has different state information

print(P.X)                      # 3 ** 2
P.X = 4
print(P.X)                      # 4 ** 2
print(Q.X)                      # 32 ** 2(1024)


'''
Notice that we’ve made two different instances—because property methods automatically
receive a self argument, they have access to the state information stored in instances.
In our case, this means the fetch computes the square of the subject instance’s
own data.
'''
